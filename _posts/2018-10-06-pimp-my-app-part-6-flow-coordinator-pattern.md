---
layout: default
title: "Pimp my app! Part 6: using Flow or Coordinator pattern"
date: 2018-10-06
---

# using Flow or Coordinator pattern instead of segue 

Apple introduce segue (`UIStoryboardSegue`) alongside storyboards in iOS 5. At first I was quite puzzled by these new tools. I was doing all my view in Objective-C code at that time, and stayed with this practice for quite some time. Even when I finally switched to storyboard, I found the segue concept quite strange, let's examine the pro and cons :

Benefits of segue: they looks nice in storyboards

Cons: Most of the time, you need to override the `prepareForSegue:sender:` method in your view controller, and 
do some setup there, like below.

```swift
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "showTranslations" {
            
            translationsController = segue.destination as? TranslationsViewController
            prepareTranslations()
            
        }
    }
```

The problem with these practice is that now your view controller is in charge of doing the
setup of the next controller in the flow. It is really a bad pattern, your view controller
should only care about the view it control (hence the name), and not about other view controllers.

The Flow pattern (sometime named Coordinator pattern) improve decoupling between view controller. There is many version of this idea, for example Soroush Khanlou  
talk about this pattern in his blog here: [Coordinators Redux](http://khanlou.com/2015/10/coordinators-redux/) .

The Flow object create, present and dismiss UIViewControllers while keeping the UIViewControllers separate and independent. Similar to how UIViewControllers manage UIViews, Flow manage UIViewControllers.

Below is how I write this in my app. 

First, you can see that the view controller has a closure named `callback` that takes an `action` enum. This is the only way the view controller communicate with the flow that controls it.
The view controller itself know nothing about other view controllers.


```swift
final class MasterViewController: UITableViewController {
    
    enum Action {
        case showDetail(fish: Fish)
        case showMenu
    }
    
    var callback: ((Action) -> ())?
```

There could be multiple flows (like "login" flow, "main" flow, "purchase" flow, etc). Here there is a single one, AppFlow.


```swift
final class AppFlow {
    
    private let navigationController: UINavigationController
    private var masterViewController: MasterViewController!
    
    init(navigationController: UINavigationController) {
        self.navigationController = navigationController
    }
    
    func start() {
        showMaster()
    }
    
    private func showMaster() {
        let controller = MainStoryboard.masterViewController
        self.masterViewController = controller
        navigationController.pushViewController(controller, animated: false)
        controller.callback = { [weak self] action in
            switch action {
            case .showDetail(let fish):
                self?.showDetail(fish: fish)
            case .showMenu:
                self?.showMenu()
            }
        }
    }
```

