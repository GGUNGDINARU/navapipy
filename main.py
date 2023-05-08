import blogapi

print('꿍디의 블로그 검색기 입니다.')
keyword = input('검색어를 입력하세요! : ')
print(f'당신이 입력한 검색어 : {keyword}')


#우리가 만든 blogapi에 keyword를 넣어서 결과를 리스트로 받기
blog_list = blogapi.get_blog_api(keyword)
for blog in blog_list:
    print(f"블로그제목 : {blog['title']}")