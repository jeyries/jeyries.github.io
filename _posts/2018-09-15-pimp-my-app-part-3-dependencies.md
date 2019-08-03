---
layout: default
title: "Pimp my app! Part 3: Dependencies"
date: 2018-09-15
---

# Dependencies

Depeendencies in the project were managed by CocoaPod. It is a pretty capable dependency manager for iOS projects, though I may prefer to use Carthage these days. Carthage is more lightweight and gives more control to the developer.

## The Podfile:

```ruby
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'
use_frameworks!

target 'Fishionary' do
    pod 'SwiftyJSON', :git => 'https://github.com/SwiftyJSON/SwiftyJSON.git'
    pod 'CHTCollectionViewWaterfallLayout'
    pod 'DownPicker'
    pod 'RxSwift',    '~> 2.0'
    pod 'RxCocoa',    '~> 2.0'
    #pod 'RxBlocking', '~> 2.0'
    #pod 'RxTests',    '~> 2.0'
    pod 'GRMustache.swift'
end
```

in 2015 RxSwift was booming. I had practiced a bit the Objective-C version: ReactiveCocoa in the past. The problem here is that I wanted to use it everywhere. Specially in this case, this framework is used only at one place in the code. RxSwift is a big dependency; it will shape the way you are doing your project so it should not be taken as a light decision. Some developers hate it with some reasons (in debug, have you ever seen how huge is a RxSwift call stack ?). Here the choice should be obvious, there is no reason at all to have it in a demo project like that.

# Moving dependencies to Carthage

The Cartfile :

```
#github "chiahsien/CHTCollectionViewWaterfallLayout"
github "u1tkzw/CHTCollectionViewWaterfallLayout" "develop"
#github "airbnb/MagazineLayout"
github "Darkseal/DownPicker"
```

Some useful Carthage commands:

    ::sh
    carthage update --no-build 

This command will make Carthage scan the dependencies in `Cartfile` and update the `Cartfile.resolved` .

    ::sh
    carthage bootstrap --cache-builds --platform iOS

This command will actually build the dependencies found in `Cartfile.resolved` .
