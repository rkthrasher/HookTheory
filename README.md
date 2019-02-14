# HookTheory
Python tool to use the HookTheory web API 


```python
from HookTheory import HookTheory

# create HookTheory instance
ht = HookTheory('your_user_name', 'your_password')

# aquire authorization so get requests to the
# HookTheory API may be made
ht.getAuth()


# try getChords(chordId) function which returns the most popular chord 
# progressions starting with chordID

ht.getChords('1,5,6').json() # returns the most likely chords to follow 
                             # the I-V-iv chord progression 
```
```
[{'child_path': '1,5,6,4',
  'chord_HTML': 'IV',
  'chord_ID': '4',
  'probability': 0.646},
 {'child_path': '1,5,6,5',
  'chord_HTML': 'V',
  'chord_ID': '5',
  'probability': 0.103}, 
  ...
  ]
  ```
  
  ```python
  
# getsongs(chordId, n) function which returns the nth page of songs 
# containing the chord progression = chordId starting with chordID

ht.getSongs('1,5,6', 1).json() # returns first page of songs containing
                               # the I-V-iv chord progression 
```
```
[{'artist': '3 Doors Down',
  'section': 'Intro',
  'song': 'Be Like That',
  'url': 'http://www.hooktheory.com/theorytab/view/3-doors-down/be...'},
 {'artist': '3 Doors Down',
  'section': 'Verse',
  'song': 'Be Like That',
  'url': 'http://www.hooktheory.com/theorytab/view/3-doors-down/be...'},
 {'artist': 'Adele',
  'section': 'Chorus',
  'song': 'Someone Like You',
  'url': 'http://www.hooktheory.com/theorytab/view/adele/someone...'}, 
  ...
  ]
  ```
