# Algorithm for the graphematic transcription of the Ursus edition

- for each 'w'
    - for each descendant text node of 'w'
        - if it's not 'expan' or another non-grapheme element
        - OPTION A
            - create a <c> (or <g>) saying that this character is a 'Grapheme'
        - OPTION B
            - create a set of graphemes in the edition
            - at the end, say that each element of the set is a 'Grapheme'
