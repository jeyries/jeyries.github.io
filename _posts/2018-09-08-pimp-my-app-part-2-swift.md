---
layout: default
title: "Pimp my app! Part 2: From Swift 2 to Swift 4"
date: 2018-09-08
---

Automatic migration from Swift 2 to Swift 4 is not available. Don't worry you can still get some help and Xcode does quite a good job at hinting you in order to perform this update.

First thing to do after opening the project is to change the build setting SWIFT_VERSION to the latest Swift version (here Swift 4.2).

Then Xcode will flag compilation error, warn about deprecated stuff, just proceed and eliminate the problems one by one.

 ![swift migration errors: do not panic ...](/images/swift migration errors.png)

Once the code compiles and run in the simulator, you can continue by adopting the latest tools that
Swift 4 provide, for example:

 - the `guard` keyword can replace a bunch of nested `let` 
 - JSON handling has improved a lot, by using the Codable protocol 

Also in 3 years, some new techniques have become popular, like MVVM (more on that latter),
whereas some other have declined in popularity, like RxSwift (IMHO).
That is why I see plenty of opportunities for refactoring this little app beyond just Swift migration.

