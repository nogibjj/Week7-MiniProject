[![Clippy](https://github.com/nogibjj/rust-data-engineering/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/rust-data-engineering/actions/workflows/lint.yml)
[![Tests](https://github.com/nogibjj/rust-data-engineering/actions/workflows/tests.yml/badge.svg)](https://github.com/nogibjj/rust-data-engineering/actions/workflows/tests.yml)


# User Guide for Caesar Cipher CLI Tool

## Project Description

This project is a command-line interface (CLI) tool written in Rust, providing functionalities to encrypt and decrypt messages using the Caesar cipher method.

## File Structure

```
/Project
|-- src
|   |-- lib.rs
|   |-- main.rs
|
|-- tests
|   |-- cipher_tests.rs
|
|-- Cargo.toml
```

## Run the CLI Tool in Rust

```bash
cargo build
cargo run
```
![image](run_result.png)

## Run the CLI Tool in Python

```bash
python main.py <message> <shift>
```
![image](python_result.png)

## Test
```bash
cargo test
```
![image](test.png)

## Makefile

Each subdirectory project uses this style to make it easy to test and run

```
format:
	cargo fmt --quiet

lint:
	cargo clippy --quiet

test:
	cargo test --quiet

run:
	cargo run 

all: format lint test run
```


## References

* [Rust Collections](https://doc.rust-lang.org/std/collections/index.html)
* [GitHub Copilot CLI](https://www.npmjs.com/package/@githubnext/github-copilot-cli)
* [Rust Fundamentals](https://github.com/alfredodeza/rust-fundamentals)
* [Rust Tutorial](https://nogibjj.github.io/rust-tutorial/)
* [Rust MLOps Template](https://github.com/nogibjj/mlops-template)
