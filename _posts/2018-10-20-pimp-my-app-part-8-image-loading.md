---
layout: post
title: "Pimp my app! Part 8: Image Loading"
date: 2018-10-20
---

You should do the loading and decoding of images in the background.

# Image Loading

There is plenty of library for doing that, for example:

- [SDWebImage](https://github.com/SDWebImage/SDWebImage)
- [Nuke](https://github.com/kean/Nuke)

However you can achive pretty good results by using 
some simple tools: NSOperationQueue for background processing, NSCache for image caching.

Here is a little `ImageLoader` class that will do the job:

```swift
final class ImageLoader {
    
    static let shared = ImageLoader()
    
    private let queue: OperationQueue
    private let imageCache = NSCache<NSString, UIImage>()
    
    private init() {
        queue = OperationQueue()
        queue.maxConcurrentOperationCount = OperationQueue.defaultMaxConcurrentOperationCount
        queue.qualityOfService = .userInitiated
    }
    
    @discardableResult
    func load(path: String, completion: @escaping (UIImage?) -> Void) -> Operation {
        let operation = BlockOperation() { [weak self] in
            let image = self?.loadSynchronously(path: path)
            DispatchQueue.main.async {
                completion(image)
            }
        }
        operation.qualityOfService = .userInitiated
        queue.addOperation(operation)
        return operation
    }
    
    func loadSynchronously(path: String) -> UIImage? {
        if let image = imageCache.object(forKey: path as NSString) {
            return image
        }
        
        guard let image = UIImage(contentsOfFile: path) else {
            return nil
        }
        
        imageCache.setObject(image, forKey: path as NSString)
        return image
    }
}
```

And here is how to use it, for example in a table view cell. Because of cell recycling, it is important to cancel first the load operation if loading is already running for a cell, before scheduling a new load operation for the current content of the cell.


```swift
final class FishCell: UITableViewCell {

    @IBOutlet weak var thumbImageView: UIImageView!

    
    private var imageOperation: Operation?
    
    func configure(fish: Fish) {
        
        imageOperation?.cancel()
        thumbImageView.image = nil
        imageOperation = ImageLoader.shared.load(path: fish.imagePath) { [weak self] image in
            self?.thumbImageView.image = image
        }
        
    }
    
}
```

