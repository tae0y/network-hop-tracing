import scapy.all as scapy
import time
import socket
import logging


"""
로깅 설정
"""
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
사용자 함수
"""
def traceroute_tcp(DEST_IPADDR, DEST_PORT, TTL_MAX, TIMEOUT_SEC):
    """
    목적지 IP, PORT로 TTL을 늘려가며 요청을 보낸다.
    실행결과를 콘솔에 출력한다.
    """
    # 출발지 IP 확인
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            SRC_IP = s.getsockname()[0]
    except Exception:
        SRC_IP = "127.0.0.1"
    logger.info(f"Traceroute started!! {SRC_IP} -> {DEST_IPADDR}:{DEST_PORT}")

    # TTL을 1부터 MAX까지 
    for ttl in range(1, TTL_MAX):
        total_elapsed = 0
        attempts_max = 3
        attempts_success_cnt = 0
        hop_ip_list = []

        for _ in range(attempts_max):
            # 요청 전송
            packet = (
                scapy.IP(dst=DEST_IPADDR, ttl=ttl, id=scapy.RandShort()) /
                scapy.TCP(dport=[DEST_PORT], flags="S") /
                scapy.Raw(load=f"GET / HTTP/1.1\r\nHost: {DEST_IPADDR}")
                # 필요시 헤더와 데이터 설정
                # scapy.Raw(load=f"GET / HTTP/1.1\r\nHost: {DEST_IPADDR}\r\n{custom_headers}\r\n\r\n{custom_data}")
            )
            start_time = time.time()
            ans, unans = scapy.sr(packet, timeout=TIMEOUT_SEC, verbose=0)
            end_time = time.time()

            # 응답 확인
            if ans:
                total_elapsed += (end_time - start_time)
                hop_ip_list.append(ans[0][1].src)
                attempts_success_cnt += 1

        # 응답이 하나라도 있는 경우 결과 출력
        if attempts_success_cnt > 0:
            avg_elapsed = total_elapsed / attempts_success_cnt
            logger.info(f"TTL: {ttl}, Average Elapsed Time: {avg_elapsed:.4f} seconds, Successful Attempts: {attempts_success_cnt}/{attempts_max}, Hop IP Addresses: {hop_ip_list}")

            # 목적지 IP에 도착한 경우 반복문 종료
            if DEST_IPADDR in hop_ip_list:
                logger.info("Reached destination!!")
                break
        else:
            logger.error(f"TTL: {ttl}, No response")


def main():
    """
    프로그램 진입점
    """
    DEST_IPADDR = socket.gethostbyname("www.naver.com")
    DEST_PORT   = 80
    TTL_MAX = 22
    TIMEOUT_SEC = 2
    traceroute_tcp(DEST_IPADDR, DEST_PORT, TTL_MAX, TIMEOUT_SEC)


if __name__ == "__main__":
    main()
