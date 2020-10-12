---
layout: post
title: "A RxSwift helper for network calls, JSON decoding and image decoding"
date: 2020-09-23
---

Summary: We propose a small helper in order to perform some classical asynchronous operations in `RxSwift` like: loading some `Data` with `URLSession`, decoding these `Data` onto some `Decodable` element or decoding these `Data` onto an `UIImage` .

# RxSwift

RxSwift is ReactiveX for Swift.

More info here: [https://github.com/ReactiveX/RxSwift](https://github.com/ReactiveX/RxSwift)

# Description

We propose a small helper in order to perform some classical operations in `RxSwift` like: loading some `Data` with `URLSession`, decoding these `Data` onto some `Decodable` element or decoding these `Data` onto an `UIImage` .

These operations can benefit from being performed asynchronously with the help of RxSwift.

The helper is made of 3 building blocks:

- `URLSession.download`: takes an `URL` and produce a `Single<Data>`
- `DecodeHelper.decode`: takes some `Data` and produce a `Single<T>` where `T` conforms to `Decodable`
- `ImageHelper.decode`: takes some `Data` and produce a `Single<UIImage>`

These building blocks can be combined with `flatMap`, like below :

```swift

class RandomUserService: RandomUserServiceProtocol {
    
    func contentObservable() -> Single<RandomUserAPI.Content> {
        
        return URLSession.shared.download(url: RandomUserAPI.url)
            .flatMap( DecodeHelper.decode )
    }
    
    
}

```

# URLSession+RxSwift.swift

This extension will help for doing network calls with RxSwift.

{% gist 7be2d1f465711b7fa736a113a4452631 %}

# DecodeHelper.swift

This module will help for doing JSON decode in RxSwift.

{% gist 25674dd81ab5315b460bf76f5dec24d2 %}

# ImageHelper.swift

This will help for doing image decode with RxSwift.

{% gist d3db83e9aca95163655f8f804ba0721c %}


