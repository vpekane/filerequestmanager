import dropbox

try:
    with open('.accesstoken') as f:
        token = f.read()
except:
    print("something went wrong")

#dropbox API
dbx = dropbox.Dropbox(token)


def file_request_objects() -> list:
    file_requests = []
    for item in dbx.file_requests_list().file_requests:
        if item.is_open:
            file_requests.append(item)

    return file_requests


def open_file_requests() -> list[dict]:
    file_requests = []
    context = {
        "id": "",
        "title": ""
    }
    items = dbx.file_requests_list().file_requests
    for item in items:
        if item.is_open:
            context["id"] = item.id
            context["title"] = item.title
            file_requests.append(context.copy())

    return file_requests


def update_file_request(id: str, title: str, destination:str) -> None:
    dbx.file_requests_update(id, title, destination)
    print("File request updated")


# def send_file_request_email() -> None:
#     pass


def get_list_of_folders() -> list[str]:
    folders = set()
    for item in dbx.file_requests_list().file_requests:
        if item.is_open:
            folders.add(item.destination)
    # pass
    list(folders)
    return folders


if __name__ == '__main__':
    pass