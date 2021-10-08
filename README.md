# worktime-calculator
worktime calculator CLI

### Install
```bash
# zshrc에 worktime alias 로 설정됩니다.
./install.sh
. ~/.zshrc
```

### Usage
10:45 AM ~ 15:59 PM 근무
...부재...
17:16 PM ~ 22:40 PM 근무
위 상황에 대한 부재시간을 빼고 근무한 시간만 계산합니다.

```bash
$ worktime
Enter the start time: 10:45
Enter the end time: 15:59
work time: 10:45 ~ 15:59
Enter the start time: 17:16
Enter the end time: 22:40
work time: 10:45 ~ 21:23
Enter the start time: ^C%
```
