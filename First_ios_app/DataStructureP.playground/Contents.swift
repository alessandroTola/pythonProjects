import UIKit
import PlaygroundSupport

class CollectionViewController : UICollectionViewController {
    var data: [String]
    
    init(data:[String], collectionViewLayout layout: UICollectionViewLayout){
        self.data = data
        super.init(collectionViewLayout: layout)
    }
    
    required init?(coder aDecoder: NSCoder) {
        self.data = []
        super.init(coder: aDecoder)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.collectionView?.backgroundColor = .white
        //self.collectionView?.register(UICollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
        self.collectionView?.register(AnimaleCollectionViewCell.self, forCellWithReuseIdentifier: "Cell")
    }
    
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return self.data.count
    }
    
    /*override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
        cell.backgroundColor = .green
        
        return cell
        
    }*/
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell:AnimaleCollectionViewCell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! AnimaleCollectionViewCell
        
        cell.backgroundColor = .green
        
        let animal = self.data[indexPath.row]
        cell.emoji = animal
        
        if self.dataMap != nil {
            cell.emoji = self.dataMap?[animal]
        } else {
            cell.emoji = animal
        }
        return cell
        
    }
    
    var dataMap:[String:String]?
}

class AnimaleCollectionViewCell : UICollectionViewCell {
    private var _label: UILabel
    
    override init(frame: CGRect) {
        let fr = CGRect(x: 0, y: 0, width: frame.size.width, height: frame.size.height)
        _label = UILabel(frame: fr)
        super.init(frame: fr)
        
        _label.text = "?"
        _label.textAlignment = NSTextAlignment.center
        addSubview(_label)
    }
    
    required init?(coder aDecoder: NSCoder) {
        _label = UILabel()
        super.init(coder: aDecoder)
        _label.text = "?"
        
        addSubview(_label)
    }
    
    public var emoji:String? {
        set {
            _label.text = newValue
        }
        
        get {
            return _label.text
        }
    }
}

var animal = ["Cat", "Dog", "Bird", "Mouse", "Elephant"]
var animalsToEmoji = ["Cat": "🐱", "Dog": "🐶", "Bird": "🐦" , "Mouse" : "🐭", "Elephant" :" 🐘","Bear":"🐻"]
var flowLayout = UICollectionViewFlowLayout()
var controller = CollectionViewController(data: animal, collectionViewLayout: flowLayout)

controller.dataMap = animalsToEmoji
PlaygroundPage.current.liveView = controller
PlaygroundPage.current.needsIndefiniteExecution = true
