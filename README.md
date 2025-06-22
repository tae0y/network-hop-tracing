# README

- 네트워크 구간별 속도를 측정하는 프로그램
- TCP 패킷에서 TTL을 1부터 22까지 늘려가며 구간별 속도측정
- 목적지 IP에 도착하면 중단

- 결과 샘플
```
INFO:__main__:Traceroute started!! {SOURCE_IP} -> 23.35.220.251:80
INFO:__main__:TTL: 1, Average Elapsed Time: 0.0072 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['192.168.219.1', '192.168.219.1', '192.168.219.1']
ERROR:__main__:TTL: 2, No response
INFO:__main__:TTL: 3, Average Elapsed Time: 0.0151 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['10.245.237.45', '10.245.237.45', '10.245.237.45']
INFO:__main__:TTL: 4, Average Elapsed Time: 0.0096 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['1.213.10.121', '1.213.10.121', '1.213.10.121']
ERROR:__main__:TTL: 5, No response
INFO:__main__:TTL: 6, Average Elapsed Time: 0.0252 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['1.213.152.150', '1.213.152.150', '1.213.152.150']
INFO:__main__:TTL: 7, Average Elapsed Time: 0.0175 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['203.229.222.101', '203.229.222.101', '203.229.222.101']
ERROR:__main__:TTL: 8, No response
ERROR:__main__:TTL: 9, No response
INFO:__main__:TTL: 10, Average Elapsed Time: 0.0149 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['112.191.125.3', '112.191.125.3', '112.191.125.3']
INFO:__main__:TTL: 11, Average Elapsed Time: 0.0169 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['112.191.125.197', '112.191.125.197', '112.191.125.197']
INFO:__main__:TTL: 12, Average Elapsed Time: 0.1998 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['183.110.64.194', '183.110.64.194', '183.110.64.194']
INFO:__main__:TTL: 13, Average Elapsed Time: 0.0112 seconds, Successful Attempts: 3/3, Hop IP Addresses: ['23.35.220.251', '23.35.220.251', '23.35.220.251']
INFO:__main__:Reached destination!!
```

## Getting Started

- 소스코드 다운로드
```
git clone {url} 
```

- 파이썬 환경설정
```
uv init
```

- 코드 실행
```
sudo uv run main.py
```
