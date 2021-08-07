//
//  ViewController.swift
//  First_ios_app
//
//  Created by Alessandro Tola on 05/02/21.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var fireButtom:UIButton!
    
    @IBOutlet var imageView:UIImageView!
    
    @IBAction func clickHandler(_ sender: UIButton) {
        let red:CGFloat = CGFloat(drand48())
        let green:CGFloat = CGFloat(drand48())
        let blue:CGFloat = CGFloat(drand48())
        
        self.view.backgroundColor = UIColor.init(red: red, green: green, blue: blue, alpha: 1)
    }
    
    
    
    @IBAction func Switch(_ sender: UISwitch) {
        imageView.isHidden = !sender.isOn
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        imageView.isHidden = true
        fireButtom.addTarget(self, action: #selector(ViewController.fireClickHandler(_:)), for: UIControl.Event.touchUpInside)
        
    }
    
    @objc func fireClickHandler(_ sender: UIButton) {
        print("Fire buttom was clicked")
        self.view.backgroundColor = UIColor.red
    }


}

