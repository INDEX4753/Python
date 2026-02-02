"""
6-11 爬虫程序实例 - 关键词信息查询

基本使用方法：
1. 运行程序：python 6-11.py
2. 输入关键词：多个关键词用空格分隔，例如 "人工智能 发展趋势"
3. 选择匹配模式：
   - 1. AND模式：所有关键词都必须匹配
   - 2. OR模式：任一关键词匹配即可
   - 3. EXACT模式：精确匹配完整短语
4. 查看结果：程序会显示搜索到的网页标题和URL

注意事项：
- 本程序使用Bing搜索引擎
- 每次搜索最多返回10条结果
- 结果会自动去重，确保信息的唯一性
"""

import requests
import re
from urllib.parse import quote

class BingSearch:
    def __init__(self, keywords, match_mode='AND'):
        self.keywords = keywords
        self.match_mode = match_mode
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.224 Safari/537.36'
        }
        self.url = self._build_url()
    
    def _build_url(self):
        if self.match_mode == 'AND':
            query = ' '.join(self.keywords)
        elif self.match_mode == 'OR':
            query = ' OR '.join(self.keywords)
        elif self.match_mode == 'EXACT':
            query = f'"{" ".join(self.keywords)}"'
        else:
            query = ' '.join(self.keywords)
        return f'https://www.bing.com/search?q={quote(query)}'
    
    def search(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.text
            else:
                print(f"搜索请求失败，状态码: {response.status_code}")
                return None
        except Exception as e:
            print(f"搜索请求出错: {str(e)}")
            return None

def get_user_input():
    """获取用户输入的关键词和匹配模式"""
    print("=== 关键词信息查询系统 ===")
    
    # 获取关键词
    keywords_input = input("请输入关键词，多个关键词用空格分隔: ")
    keywords = [keyword.strip() for keyword in keywords_input.split() if keyword.strip()]
    
    if not keywords:
        print("错误: 请至少输入一个关键词")
        return None, None
    
    # 获取匹配模式
    print("\n请选择关键词匹配模式:")
    print("1. AND模式 (所有关键词都必须匹配)")
    print("2. OR模式 (任一关键词匹配即可)")
    print("3. EXACT模式 (精确匹配完整短语)")
    
    mode_choice = input("请输入模式编号 (1-3): ")
    match_mode_map = {
        '1': 'AND',
        '2': 'OR',
        '3': 'EXACT'
    }
    
    match_mode = match_mode_map.get(mode_choice, 'AND')
    
    print(f"\n已设置: 关键词={keywords}, 匹配模式={match_mode}")
    return keywords, match_mode

def parse_search_results(html_content):
    """解析搜索结果，提取相关信息"""
    if not html_content:
        return []
    
    results = []
    
    # 使用更精确的正则表达式提取Bing搜索结果
    # 匹配Bing特有的搜索结果格式
    bing_pattern = re.compile(r'<li[^>]*class="b_algo"[^>]*>.*?<h2[^>]*>.*?<a[^>]*href="(https?://[^"<>]+)"[^>]*>(.*?)</a>.*?</h2>', re.DOTALL)
    matches = bing_pattern.findall(html_content)
    
    if matches:
        for link, title in matches:
            # 清理标题
            title = re.sub('<.*?>', '', title)
            title = title.strip()
            
            if title and len(title) > 10:
                results.append({
                    'title': title,
                    'url': link
                })
    
    # 如果没有匹配到，使用通用模式
    if not results:
        generic_pattern = re.compile(r'<a[^>]*href="(https?://[^"<>]+)"[^>]*>(.*?)</a>', re.DOTALL)
        generic_matches = generic_pattern.findall(html_content)
        
        for link, title in generic_matches:
            # 过滤掉不需要的链接
            if 'bing.com' in link or not link.startswith('http'):
                continue
            
            # 清理标题
            title = re.sub('<.*?>', '', title)
            title = title.strip()
            
            # 过滤掉域名形式的标题
            if title and len(title) > 10 and not title.startswith('http') and '.' not in title[:10]:
                results.append({
                    'title': title,
                    'url': link
                })
    
    # 去重并限制结果数量
    unique_results = []
    seen_urls = set()
    for result in results:
        if result['url'] not in seen_urls:
            seen_urls.add(result['url'])
            unique_results.append(result)
    
    return unique_results[:10]

def main():
    """主函数，协调各个模块的工作"""
    # 获取用户输入
    keywords, match_mode = get_user_input()
    
    if not keywords:
        return
    
    # 创建搜索引擎实例
    searcher = BingSearch(keywords, match_mode)
    
    # 执行搜索
    print("\n正在搜索相关信息...")
    html_content = searcher.search()
    
    if not html_content:
        print("搜索失败，无法获取结果")
        return
    
    # 解析搜索结果
    search_results = parse_search_results(html_content)
    
    if not search_results:
        print("未能解析到搜索结果")
        return
    
    # 展示搜索结果
    print("\n=== 搜索结果 ===")
    for i, result in enumerate(search_results, 1):
        print(f"{i}. {result['title']}")
        print(f"   链接: {result['url']}")
        print()
    
    print("\n=== 任务完成 ===")

# 程序入口
if __name__ == "__main__":
    main()
