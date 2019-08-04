---
layout: post
title: "Pimp my app! Part 5: Supporting the iPad"
date: 2018-09-29
---

Sometimes you need to take a decision about which devices or form factor your app will support. This can have a big impact on test and development time.

# Supporting the iPad

The initial customer for this app wanted to support the iPad. It could be a perfect valid choice, even if we could wonder if people that go fishing takes their iPad with them. 
Probably they rather go fishing with a phone than a tablet.

Anyway, as I convert this app to an exercice aimed at instructional purpose, let's not be distracted by the support of multiple device form factor. Maybe that will be a goal for a future tutorial.
So I will remove the `UISplitViewController` and reduce the list of supported devices and orientations.

Also supporting multiple interface orientations has some impact on the development time and should be considered carefully. Most people are fine using their iPhone app in portrait only mode.

There is plenty of books explaining how to build a MVP - Minimum Viable Product - In our case the decision is straightforward.

There is one exception here, displaying the fullscreen image of a fish works better in landscape, 
so I decided to keep only this view in landscape mode in a mostly portrait mode app, see `ImageViewController`.

For this, you just need to override the `supportedInterfaceOrientations` property, like this:

```swift
    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        return .landscape
    }
```


