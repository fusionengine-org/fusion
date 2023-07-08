use gtk::*;
use gtk::prelude::*;


pub fn menu(window: &ApplicationWindow) {
    
    let button = Button::with_label("Click me!");
    button.connect_clicked(|_| {
        eprintln!("Clicked!");
    });
    window.set_child(Some(&button));
}