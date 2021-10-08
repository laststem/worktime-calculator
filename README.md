# worktime-calculator
worktime calculator CLI

### Description
- 근무 시간을 입력하면 부재 시간을 빼고 계산해줍니다.

### Install
```bash
# zshrc에 worktime alias 로 설정됩니다.
./install.sh
. ~/.zshrc
```

### Usage
```bash
# 10:45 AM ~ 15:59 PM 근무
# ...부재...
# 17:16 PM ~ 22:40 PM 근무 

$ worktime
Enter the start time: 10:45
Enter the end time: 15:59
> work time: 10:45 ~ 15:59
Enter the start time: 17:16
Enter the end time: 22:40
> work time: 10:45 ~ 21:23
Enter the start time: ^C% 
```
