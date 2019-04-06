

def reduce_file_path(path):
    file_path = path

    file_path = ''.join([file_path[index] for index 
                                  in range(len(file_path)-1) if file_path[index+1] != file_path[index] 
                                  or file_path[index]!="/"]+[file_path[-1]])

    while '..' in file_path:
        
        dotsPosition = file_path.rfind('..')
        if dotsPosition == 1:
            file_path = file_path[3:]
            break
        
        file_path = file_path[:dotsPosition-1] + file_path[(dotsPosition+4):]
        
        while True:
            file_path = file_path[:dotsPosition-1]
            if file_path.endswith("/"):                
                break;
            dotsPosition -=1

    file_path = file_path.replace('./','')

    if len(file_path)>1 and file_path[-1:]=="/":
        file_path = file_path[:-1]  

    return file_path



def main():
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))


if __name__ == '__main__':
    main()