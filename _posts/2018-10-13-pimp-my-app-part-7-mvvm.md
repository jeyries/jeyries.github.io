---
layout: post
title: "Pimp my app! Part 7: MVVM"
date: 2018-10-13
---

# MVVM

Model - View - View Model

- reduce view controller size
- improve testability

Here is a brief summary:

MVC (Model - View - Controller) is a good and mature paradigm. Usually this is a good starting point for a new screen.
However, as view complexity increase over time, it is sometimes good to extract some of the presentation logic of the view controller into an other object, the view model. 
As the name implies it is a model which purpose is to compute and store all the information needed for the view: 
strings or attributed strings for label, provide image for image view, etc ..
This paradigm is called MVVM (Model - View - ViewModel)

More info here: [MVVM on Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)

in my project, I had a DetailViewController that could benefit a bit of refactor. I extracted most of the presentation logic into a view model named DetailViewModel.

```swift
final class DetailViewModel {
    
    private let fish: Fish
    
    convenience init() {
        self.init(fish: DetailViewModel.defaultFish)
    }
    
    init(fish: Fish) {
        self.fish = fish
    }
    
    var title: String {
        let source = ConfigManager.shared.source
        let name = fish.name(target: source)
        let source_prop = DataManager.shared.search_prop(name: source)!
        return "\(name) (\(source_prop.header))"
    }
    
    var name: String {
        let target = ConfigManager.shared.target
        return fish.name(target: target)
    }

    ...
```

As a result, the size of the view controller was 200 lines before and is reduced to 130 lines now. Of course, you can expect greater size reduction for more complex view controller.

Size and therefore complexity reduction is not the only benefit; Also it is much more easy to unit test the view model than the view controller itself (More on that latter).

