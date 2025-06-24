import re

def extract_usernames_and_links(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    # Ambil username dan link lengkap
    pattern = r'<a[^>]+href="(https://www.instagram.com/([\w\.]+))"[^>]*>'
    return dict(re.findall(pattern, html))

def extract_usernames(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    usernames = set(re.findall(r'instagram.com/([\w\.]+)', html))
    return usernames

if __name__ == "__main__":
    followers = extract_usernames('followers_1.html')  # yang mengikuti Anda
    following_links = extract_usernames_and_links('following.html')  # yang Anda ikuti (username & link)
    following = set(following_links.keys())

    not_following_back = following - followers

    with open('tidak_followback.html', 'w', encoding='utf-8') as out:
        out.write('<html><head><title>Tidak Followback</title></head><body>')
        out.write('<h2>Akun yang Anda ikuti tetapi tidak mengikuti Anda kembali:</h2>')
        out.write('<ul>')
        for link in sorted(not_following_back):
            url = following_links[link]
            out.write(f'<li><a href="{url}" target="_blank">{link}</a></li>')
        out.write('</ul></body></html>')
    print("Daftar sudah disimpan di file 'tidak_followback.html'")
