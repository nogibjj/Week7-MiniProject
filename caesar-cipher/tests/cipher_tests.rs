// This statement is required to bring your library into scope.
// "caesar_cipher" should be replaced with the name you've defined for your library in your Cargo.toml.
use caesar_cipher::*;

#[test]
fn test_encrypt() {
    let text = "hello";
    let shift = 3;
    assert_eq!("khoor", encrypt(text, shift));
}

#[test]
fn test_decrypt() {
    let text = "khoor";
    let shift = 3;
    assert_eq!("hello", decrypt(text, shift));
}

#[test]
fn test_encrypt_decrypt() {
    let text = "hello, world!";
    let shift = 5;
    let encrypted = encrypt(text, shift);
    let decrypted = decrypt(&encrypted, shift);
    assert_eq!(text, decrypted);
}
// ... more tests
