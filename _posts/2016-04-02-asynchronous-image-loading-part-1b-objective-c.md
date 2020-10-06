---
layout: post
title: "How to load images asynchronously ? adding associated objects."
date: 2016-04-02
---

Summary: How to load images asynchronously ? adding associated objects.

# Description

How to load images asynchronously on iOS ? Here is a way to do this with UIKit in Objective-C using ReactiveCocoa and associated objects.

Note: I wrote this code in 2016 for an interview with a company. This is only for educational purpose.

# Associated Objects

Associated Objects—or Associative References, as they were originally known—are a feature of the Objective-C 2.0 runtime, introduced in OS X Snow Leopard (available in iOS 4). The term refers to the following three C functions declared in `<objc/runtime.h>`, which allow objects to associate arbitrary values for keys at runtime:

```
- objc_setAssociatedObject
- objc_getAssociatedObject
- objc_removeAssociatedObjects
```

Why is this useful? It allows developers to add custom properties to existing classes in categories, which is an otherwise notable shortcoming for Objective-C.

More info about that on [NSHipster](https://nshipster.com/associated-objects/) .

#  UIImageView+DZRImageManager.h

The header is pretty simple. We hide all the internal of this category on `UIImageView` and there is only 1 methods. 

- `dzr_setImageWithURL`: This property set the image that will be asynchronously loaded onto the `UIImageView`.

{% gist a894c79af595117d57a6dc62d0656cd9 %}

# UIImageView+DZRImageManager.m

This category relies on the previously described `DZRImageManager` for doing the image loading work. 

The objective-C runtime is used in order to retain the ReactiveCocoa `disposable` with the `UIImageView` .

{% gist d78714336433898f4ce1b9ccfaafff17 %}


