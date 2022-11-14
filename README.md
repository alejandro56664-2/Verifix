# Verifix: Verified Repair of Programming Assignments

## Contributors:
### Authors
Umair Z. Ahmed*, Zhiyu Fan*, Jooyong Yi, Omar I. Al-Bataineh, Abhik Roychoudhury

### Principal Investigator
Abhik Roychoudhury

## Publication
To be update

## Supported system and language

- Ubuntu > 16.04
- Python > 3.8


## Setup

1. Prerequisite packages
- clang > 12.0.0
- pip3
- [clara](https://github.com/iradicek/clara)
```
sudo apt update
sudo apt install clang-12
sudo apt install python3-pip
alias clang="clang-12"
```

2. Install dependencies
```
pip3 install -r requirements.txt
```

## Running Verifix
```
python3 -m main -m repair -pc data/examples/simple_correct.c -pi data/examples/simple_incorrect.c -tc data/examples/simple_tests/
```

```
python3 -m main -m repair -pc data/examples/check_prime_correct.c -pi data/examples/check_prime_incorrect.c -tc data/examples/check_prime_tests/
```


```
python3 -m debugpy --listen 5678 main.py -m repair -pc data/uncode/examples/p7_calc_pi_reference.py -pi data/uncode/examples/p7_calc_pi_failed.py -tc data/uncode/examples/p7_calc_pi_test/ -debug t
```