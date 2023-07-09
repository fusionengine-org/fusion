use gtk::prelude::*;
use gtk::*;

pub fn menu(window: &ApplicationWindow) {
    let button = Bon::with_label("Click me!");
    button.connect_clicked(|button| {
        button.set_label("Hello World!");
    });
    window.set_child(Some(&button));
}
