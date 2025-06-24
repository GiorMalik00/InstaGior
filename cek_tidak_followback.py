import re

def extract_usernames(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    # Asumsi username ada dalam href ke instagram.com/username
    usernames = set(re.findall(r'instagram.com/([\w\.]+)', html))
    return usernames

if __name__ == "__main__":
    followers = extract_usernames('followers_1.html')  # yang mengikuti Anda
    following = extract_usernames('following.html')    # yang Anda ikuti

    not_following_back = following - followers

    with open('tidak_followback.txt', 'w', encoding='utf-8') as out:
        out.write("Akun yang Anda ikuti tetapi tidak mengikuti Anda kembali:\n")
        for user in sorted(not_following_back):
            out.write(user + '\n')
    print("Daftar sudah disimpan di file 'tidak_followback.txt'")
