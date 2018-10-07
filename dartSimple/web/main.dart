import 'dart:html';

void main() {
  ButtonInputElement submit = querySelector("#submit");
  NumberInputElement age = querySelector("#age");
  TextInputElement name  = querySelector("#name");
  name.onClick.listen((MouseEvent e) => name.value = "");
  submit.onClick.listen((MouseEvent e) {
    window.alert("hi ${name.value} your age is  ${age.value}");
  });
  querySelector('#output').text = 'Your Dart app is running.';
}
