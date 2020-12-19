## Tasks:
### 1. Create path ~/f1/f2/f3/f4/f5/f6; Create and fill in text file in f1 folder; Copy it to f6 folder; Navigate to Home folder; Find copied file and remove it
```shell
$ mkdir -p ~/f1/f2/f3/f4/f5/f6
$ cd ~/f1
$ echo "Some text" > textfile.txt
$ cp textfile.txt ~/f1/f2/f3/f4/f5/f6/
$ cd
$ find -iname textfile.txt
$ rm -f ~/f1/f2/f3/f4/f5/f6/textfile.txt
```
### 2. Redirect errors only output into separate file
```shell
$ find -iname textfile.txt 2> errors_output.txt
```

### 3. Redirect error and standart outputs into separate file
```shell
$ find -iname textfile.txt &> command_output.txt
```

### 4. Create file, change owner to root. Add permissions to execute file
```shell
$ touch somefile.txt
$ sudo chown root somefile.txt
$ sudo chmod +x somefile.txt
```

### 5. make cmd2 executes only if cmd1 fails
```shell
$ cmd1 || cmd2
```

### 6. make cmd2 executes only if cmd1 successful
```shell
$ cmd1 && cmd2
```

### 7. Create and execute sh file that prints current folder. NOTE: Do not use any text redactor
```shell
$ touch working_directory_printer.sh
$ echo "pwd" > working_directory_printer.sh
$ chmod +x working_directory_printer.sh
$ ./working_directory_printer.sh
```