use gtk::prelude::*;
use gtk::*;

pub fn menu(window: &ApplicationWindow) {
    let button = Button::builder()
        .label("Press me!")
        .margin_top(12)
        .margin_bottom(12)
        .margin_start(12)
        .margin_end(12)
        .build();
    button.connect_clicked(|button| {
        button.set_label("Hello World!");
    });
    window.set_child(Some(&button));
}
