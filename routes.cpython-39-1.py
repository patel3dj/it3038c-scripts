a
    98?a  ?                   @   s?   d dl mZmZmZ d dlmZ ee?Zej?e? e?	d?dd? ?Z
ej	ddgd?d	d
? ?Zej	ddgd?dd? ?Zej	ddgd?dd? ?Zej	ddgd?dd? ?Zej	ddgd?dd? ?Zej	ddgd?dd? ?Zej	ddgd?dd? ?ZdS )?    )?Flask?render_template?request)r   ?/c                   C   s   t d?S )Nz
index.html)r   ? r   r   ?"C:\it3038c-scripts\flask\routes.py?hello   s    r   z/welcomeZPOST)?methodsc                   C   s   t dtjd d?S )N?welcome.html?myName)r   ?r   r   ?formr   r   r   r   ?welcome   s    r   z/backc                   C   s   t dtjd d?S )Nz	back.html?getBack)r   r   r   r   r   r   ?back   s    r   z/sportc                   C   s   t dtjd d?S )Nzsports.html?getSport)r   r   r   r   r   r   ?sport   s    r   z/collegec                   C   s   t dtjd d?S )Nzcollege.html?
getCollege)r   r   r   r   r   r   ?college   s    r   z/hobbyc                   C   s   t dtjd d?S )Nz
hobby.html?getHobby)r   r   r   r   r   r   ?hobby   s    r   z/sportscontc                   C   s   t dtjd d?S )Nzsportscont.html?getSportscont)r   r   r   r   r   r   ?
sportscont   s    r   z/fifac                  C   s0   t jd } | dkrtd?S tdt jd d?S d S )N?getfifaZyesr
   z	fifa.html?r   )r   r   r   r   r   r   r   ?fifa#   s    
r   N)Zflaskr   r   r   Zflask.globals?__name__?appZconfigZfrom_objectZrouter   r   r   r   r   r   r   r   r   r   r   r   ?<module>   s&   






