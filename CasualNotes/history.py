# -*- coding: utf-8 -*-


import json
from pathlib import Path
import requests
# 禁用不安全请求警告（访问自签名证书接口时用，可选）
requests.packages.urllib3.disable_warnings()


OUTPUT_FILE_COUNT = 3
OUTPUT_FILE_TEMPLATE = "data_part{index}.json"


def write_json_parts(data, file_count=OUTPUT_FILE_COUNT):
    base_size, remainder = divmod(len(data), file_count)
    start = 0

    for index in range(file_count):
        current_size = base_size + (1 if index < remainder else 0)
        chunk = data[start:start + current_size]
        file_path = Path(OUTPUT_FILE_TEMPLATE.format(index=index + 1))
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=4)
        start += current_size

def send_form_request(startTime, endTime):
    # ====================== 替换为你的实际参数 ======================
    # 1. 请求URL
    url = "https://www.sui.com/tally/new.rmi"
    
    # 2. 请求头（必须包含指定的Content-Type）
    headers = {
        "sec-ch-ua-platform": "Windows",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        # "Postman-Token": "3b583435-512f-46d1-a187-6acdac5b9871"
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    
    # 3. Cookies（会话/登录凭证，无则留空字典）
    cookies = {
        "SESSION": "a65c4af9-d506-4f4d-9b9f-2620f3c03f1c",
        "SESSION_COOKIE": "d9e21fbbd853e2d89543561dfe485965",
        "_3d_tips": "=1",
        "__spm_bid": "64e98ba82ccbsb43p052b86453m3b195",
        "closeGuide": "1"
    }
    
    # 4. 请求体（表单格式，字典类型，会自动编码为x-www-form-urlencoded格式）
    body = {
        "beginDate": startTime,
        "endDate": endTime,
        "bids": "0",
        "cids": "0",
        "isDesc": "0",
        "memids": "0",
        "mids": "0",
        "note": "",
        "opt": "list2",
        "order": "tran_time",
        "page": 1,
        "pids": "0",
        "sids": "0",
    }
    # ===============================================================
    
    try:
        curPage = 1
        maxPage = 2
        res = []
        while curPage <= maxPage:
            body["page"] = curPage
            # POST请求（适配x-www-form-urlencoded格式）
            response = requests.post(
                url=url,
                headers=headers,
                cookies=cookies,
                data=body,  # 核心：用data参数而非json参数
                verify=False,  # 忽略SSL证书验证（内网/自签名证书接口用）
                timeout=10  # 10秒超时，避免脚本卡死
            )
            
            # 解析JSON响应（如果接口返回JSON）
            try:
                response_json = response.json()
                maxPage = response_json.get("pageCount", 1)
                # print(len(response_json.get("groups", [])))
                res.extend(response_json.get("groups", []))
                # print("解析后的JSON响应：", response_json)
            except Exception as e:
                print("提示：响应不是JSON格式，解析失败（非错误）：", e)

            import time
            time.sleep(1)  # 间隔1秒
            curPage = curPage + 1
        write_json_parts(res)
    except requests.exceptions.Timeout:
        print("❌ 请求超时！请检查网络或接口响应速度")
    except requests.exceptions.ConnectionError:
        print("❌ 连接失败！请检查URL是否正确、网络是否通畅")
    except Exception as e:
        print("❌ 请求异常：", str(e))


if __name__ == "__main__":
    # 执行单次请求
    send_form_request("2017.1.1", "2026.2.1")
    
    # 如果需要批量执行，取消下面的注释
    # batch_send_form_request()
