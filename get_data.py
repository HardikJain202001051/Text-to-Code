def main_sync():
    import asyncio

    from github import Github
    import time
    import datetime
    import os
    ACCESS_TOKEN = "" #open('token.txt').read()
    g = Github(ACCESS_TOKEN)

    def git_clone(repository):
        os.system(f'git clone {repository.clone_url} D:\\MajorProject\\repos\\{repository.owner.login}\\{repository.name}')

    def main():
        end_time = time.time() -86400*2
        start_time = end_time - 86400
        no_of_days = 50
        # tasks = []
        try:
            for i in range(1,no_of_days+1):
                start_time_str = datetime.datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
                end_time_str = datetime.datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
                query = f'react language:JavaScript created:{start_time_str}..{end_time_str}'
                end_time -= 86400
                start_time -= 86400
                result = g.search_repositories(query)
                print(result.totalCount)
                for idx,repository in enumerate(result):
                    # print(f'{repository.clone_url}')
                    # print(f'{repository.owner.login}')
                    # tasks.append(git_clone(repository))
                    print(idx,end=' ')
                    os.system(f'git clone {repository.clone_url} D:\\MajorProject\\repos\\{repository.owner.login}\\{repository.name}')
                print(f"Day {i}\n")
                time.sleep(60)
        except Exception as e:
            print(str(e))
            print('...\n....\n...\n....\n:(\n')
            print(f"Day {i}\n")
            print(start_time)
            time.sleep(300)

    main()

main_sync()
