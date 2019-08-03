---
layout: default
title: "Pimp my app! Part 9: Storyboard identifiers"
date: 2018-10-27
---

# Storyboard identifiers

Storyboards lets you instantiate your view controller with a specific identifier. This identifier is a unique string.

 ![Storyboard identifiers](/images/storyboard-id.png)

The problem with that is that you can have a wrong or obsolete identifiers. Furthermore Swift is a strongly typed language so it would be nice to also have the precise type of the view controller, instead of a generic `UIViewController`.

There is precisely, a great tool for this task,
[SwiftGen](https://github.com/SwiftGen/SwiftGen). The punchline for this tool is :

> The Swift code generator for your assets, storyboards, Localizable.strings, … — Get rid of all String-based APIs! 

For instructional purpose, and because my app is small, here is how I achieve the same result with a simple class:

```swift
struct MainStoryboard {
    
    static var storyboard: UIStoryboard {
        let bundle = Bundle.main
        return UIStoryboard(name: "Main", bundle: bundle)
    }
    
    static var masterViewController: MasterViewController {
        return storyboard.instantiateViewController(withIdentifier: "master-scene") as! MasterViewController
    }
    
    static var detailViewController: DetailViewController {
        return storyboard.instantiateViewController(withIdentifier: "detail-scene") as! DetailViewController
    }
    
    static var imageViewController: ImageViewController {
        return storyboard.instantiateViewController(withIdentifier: "image-scene") as! ImageViewController
    }
    
    static var settingsViewController: UIViewController {
        return storyboard.instantiateViewController(withIdentifier: "settings-navigation")
    }
}
```

