---
layout: post
title: "Pimp my app! Part 4: HTML Rendering"
date: 2018-09-22
---

A web view has been the usual solution when you want to render text with formatting and links. However UIWebView has been deprecated since a long time, it is time to switch. WKWebView is a no brainer, the change is easy. 

Furthermore, in my case, I was using a web view just for rendering some attributed text with sometime a link in it, maybe something cleaner can be done ? Also, web view take some time to display at first, this could be replaced by an NSAttributedString.

# Rendering HTML into an NSAttributedString

At some point, every iOS developer will encounter this situation: you need to display some text that is provided with some HTML formating. 
Also this text can have some HTML link in it and user should be able to follow the link.
Here I had choosen to use a version of the Mustache library for performing this task.

The template looks like that:

{% raw %}
```html
<html>
<style type="text/css">
body {
    font-family: "-apple-system", "sans-serif";
    font-size: 14px;
}
h2 {
    font-size: 17px;
}
</style>
<body>
    <hr>
    <h2>Concern :</h2>
    <p>{{{concern}}}</p>
</body>
</html>
```
{% endraw %}

First problem, the GRMustache.swift library is not maintened anymore and does not compile with Swift 4.
Ok, I can switch back to the GRMustache library in Objective-C.

Or I could use a more supported template renderer like [Stencil](https://github.com/stencilproject/Stencil).

Then I realized that after all, it is a bit of overkill, because nowadays we have multi-line strings in Swift and the string interpolation can perfectly do the job:

```swift
struct SimpleRenderer {
    static func render(concern: String) -> String {
        return """
<html>
<style type="text/css">
body {
    font-family: "-apple-system", "sans-serif";
    font-size: 14px;
}
h2 {
    font-size: 17px;
}
</style>
<body>
    <hr>
    <h2>Concern :</h2>
    <p>\(concern)</p>
</body>
</html>
"""
    }
}
```

Next step: after all, do we really need to instantiate a web view (WKWebView) just for rendering some text ?
We can use NSAttributedString for that task !

```swift
let options = [NSAttributedString.DocumentReadingOptionKey.documentType:
                        NSAttributedString.DocumentType.html]

let attributedString = try? NSMutableAttributedString(data:htmlData,
                                                        options: options,
                                                        documentAttributes: nil)
```

Then how to get the link ? Easy, NSAttributedString has already done the parsing of the HTML, we can retrieve the link from it:

```swift
extension NSAttributedString {
    var links: [URL] {
        var links = [URL]()
        self.enumerateAttribute(.link, in: NSRange(0..<self.length), options: []) { value, range, stop in
            if let value = value as? URL {
                links.append(value)
            }
        }
        return links
    }
}
```

now you can install a UITapGestureRecognizer on the label, and open a Safari view when the user tap the label.

```swift
        detailConcernLabel.attributedText = attributedString
        detailConcernLabel.isUserInteractionEnabled = true
        detailConcernLabel.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(tapConcern)))

    @objc func tapConcern() {
        let attributedString = detailConcernLabel.attributedText!
        guard let link = attributedString.links.first else { return }
        let safariVC = SFSafariViewController(url: link)
        present(safariVC, animated: true, completion: nil)
    }
```

