---
layout: post
title: "How to load images asynchronously ? - UIKit in Objective-C using ReactiveCocoa"
date: 2016-04-01
---

Summary: How to load images asynchronously ? - UIKit in Objective-C using ReactiveCocoa

# Description

How to load images asynchronously on iOS ? Here is a way to do this with UIKit in Objective-C using ReactiveCocoa 

Note: I wrote this code in 2016 for an interview with a company. This is only for educational purpose.

# ReactiveCocoa

[ReactiveCocoa](https://github.com/ReactiveCocoa/ReactiveCocoa/tree/2.x-maintenance) is an Objective-C framework inspired by Functional Reactive Programming. It provides APIs for composing and transforming streams of values.

# DZRImageManager.h

The header is pretty simple. We hide all the internal of this class and there is only 2 public methods. 

- `sharedInstance`: This property return the shared instance of this singleton.
- `fetch`: this method returns the result of fetching the image at the provided url

{% gist 3ca1f69186c3986fbcc6b6d372c8fdd7 %}

# DZRImageManager.m

The implementation relies on `NSURLSession` for the downloading and on `NSCache` for caching decoded images. Also there is an extra `NSURLCache` that is used in order to cache the network responses.

The `fetch` method use `flattenMap` to combine the result of 2 operations: 

- `download`: does the download in the background
- `decode`: decode the image in the background

{% gist 888e98ee0c9973336c599e8464026428 %}


