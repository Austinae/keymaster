## keymaster - password generator to help keep passwords safe

<div align="center">
<img align="center" src="https://github.com/Austinae/KeyMaster/assets/44261381/08fbfd0c-f897-407b-bf5e-abe3b2007808" width="400px" />
</div>

### Installation
Clone the repository locally.
```bash
git clone git@github.com:Austinae/keymaster.git
```

For ease of use, I recommend you add an alias to your PATH environment.
```bash
alias keymaster="py /path/to/this/repository/keymaster/src/keymaster.py"
# Refresh your terminal and now you can use it as follows
keymaster -l 20 -ns
```


### Documentation
```bash
usage: Password Generator [-h] [-nu] [-nl] [-nn] [-ns] [-cs CUSTOM_SYMBOLS] [-l LENGTH]

What the program does

options:
  -h, --help            show this help message and exit
  -nu, --no-uppercase   Password will not contain uppercase characters
  -nl, --no-lowercase   Password will not contain lowercase characters
  -nn, --no-numbers     Password will not contain numbers
  -ns, --no-symbols     Password will not contain default symbols *^!@#$?/[]+_]
  -cs CUSTOM_SYMBOLS, --custom-symbols CUSTOM_SYMBOLS
  		Custom set of symbols for your password, takes precedence on default symbols
  -l LENGTH, --length LENGTH
  		The length of the password
```

### Example use cases

Generate password with 20 characters, with custom symbols *, $, /, =, £ , ',' and ?

`py keymaster.py -l 20 -cs '*$/=£,?'` => zdBMSnE/JfpE3$G?vsu

Generate password with 14 characters, no numbers and no symbols.

`py keymaster.py -l 14 -nn -ns`
=> AwwtzcOramhTSy

### General advice relating to passwords

###### A good password should not:

- Be shared across unprotected communication channels
- Be used across platforms
- Contain personal information that can be traced back to you
- Contain words, names or technical jargon, even through substitutions such as the following

```
$, S or 5 for s
1, I or ! for i
@ or A for a
7 or T for t
3 or E for e
9, G or 6 for g
0 or O for o
8 or B for b
```

###### A password should contain a random combination of:

- Uppercase letters: A-Z
- Lowercase letters: a-z
- Numbers: 0-9
- Symbols:  *^!@#$?/[]+_] (these are the ones I chose, can be changed using cs flag)

###### Password storage

Most people store passwords either on a notepad file or an excel document without any protection, this is **not secure**. If an intruder gets access to this file either physically or virtually, these aren't encrypted and the personal data behind will be exposed.

A better way of storing your passwords. Download veracrypt and create an encrypted volume using either SHA-256 or SHA-512. Encrypt your [excel workbook](https://www.boisestate.edu/oit-itgrc/it-standards-category/how-to-encrypt-or-protect-an-excel-file/). If you are on a mac, this provides three layers of protection, (a) the OS level, macOS encrypt by default your drive, (b) your encryped volume, (c) your encrypted Excel workbook.

### Next steps

- Use swift to create a build which can run in the menu bar, start [here?](https://www.youtube.com/watch?v=CuMLpnjPr2Y), look into how I can deploy this on the app store.
- Transform this into a library which can be installed with apt / brew.
