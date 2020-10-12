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

- `NetworkHelper.download`: takes an `URL` and produce a `Single<Data>`
- `NetworkHelper.decode`: takes some `Data` and produce a `Single<T>` where `T` conforms to `Decodable`
- `ImageHelper.decode`: takes some `Data` and produce a `Single<UIImage>`

These building blocks can be combined with `flatMap`, like below :

```swift

class RandomUserService: RandomUserServiceProtocol {
    
    func contentObservable() -> Single<RandomUserAPI.Content> {
        
        return NetworkHelper.download(url: RandomUserAPI.url)
            .flatMap( NetworkHelper.decode )
    }
    
    
}

```



# NetworkHelper.swift

This will help for doing network calls with RxSwift.

{% gist a86a04fa0aa653bb6699f41411c2e91c %}

# ImageHelper.swift

This will help for doing image decode with RxSwift.

{% gist ca57b926f43709d467bc36172578116d %}


