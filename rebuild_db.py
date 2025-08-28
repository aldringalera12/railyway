#!/usr/bin/env python3
"""
Rebuild vector database for Railway deployment
This script rebuilds the vector database if it doesn't exist or is corrupted.
"""

import os
import sys
from definition_chunker import DefinitionChunker

def rebuild_database():
    """Rebuild the vector database with essential PRMSU data."""
    print("🔄 Rebuilding vector database...")
    
    # Initialize chunker
    chunker = DefinitionChunker(
        db_path="./vector_db",
        collection_name="definitions"
    )
    
    # Essential PRMSU definitions
    essential_definitions = [
        {
            'term': 'PRMSU',
            'definition': 'President Ramon Magsaysay State University (PRMSU) is a state university located in Iba, Zambales, Philippines. It was officially established by Republic Act No. 11015 on April 20, 2018.',
            'full_text': 'PRMSU: President Ramon Magsaysay State University (PRMSU) is a state university located in Iba, Zambales, Philippines. It was officially established by Republic Act No. 11015 on April 20, 2018.',
            'type': 'definition'
        },
        {
            'term': 'Cross Enrolment Types',
            'definition': 'The four types of cross-enrolment at PRMSU are: 1) Inbound Cross Enrolment (students from other institutions enrolling at PRMSU), 2) Outbound Cross Enrolment (PRMSU students enrolling in external institutions), 3) In-Campus Cross Enrolment (PRMSU students enrolling in different colleges within the same campus), and 4) Out-Campus Cross Enrolment (PRMSU students enrolling in another PRMSU campus).',
            'full_text': 'Cross Enrolment Types: The four types of cross-enrolment at PRMSU are: 1) Inbound Cross Enrolment, 2) Outbound Cross Enrolment, 3) In-Campus Cross Enrolment, and 4) Out-Campus Cross Enrolment.',
            'type': 'definition'
        },
        {
            'term': 'Midyear Units',
            'definition': 'Students may take a maximum of 9 units during midyear classes. Graduating students may overload up to 12 units only with approval from the Registrar upon recommendation of the Dean.',
            'full_text': 'Midyear Units: Students may take a maximum of 9 units during midyear classes. Graduating students may overload up to 12 units only with approval from the Registrar upon recommendation of the Dean.',
            'type': 'definition'
        },
        {
            'term': 'Absence Policy',
            'definition': 'Students who accumulate 20% unexcused absences in any subject automatically receive a grade of 5.0 (failing grade) for that subject.',
            'full_text': 'Absence Policy: Students who accumulate 20% unexcused absences in any subject automatically receive a grade of 5.0 (failing grade) for that subject.',
            'type': 'definition'
        },
        {
            'term': 'Uniform Policy',
            'definition': 'Male students must wear white polo shirt, black pants, and black formal shoes. Female students must wear blue skirt or blue slacks, white blouse, necktie, and black shoes.',
            'full_text': 'Uniform Policy: Male students must wear white polo shirt, black pants, and black formal shoes. Female students must wear blue skirt or blue slacks, white blouse, necktie, and black shoes.',
            'type': 'definition'
        }
    ]
    
    # Store definitions
    try:
        stored_count = chunker.store_chunks(essential_definitions, "rebuild_script")
        print(f"✅ Successfully stored {stored_count} definitions")
        
        # Verify storage
        all_definitions = chunker.list_all_definitions()
        print(f"📊 Database now contains {len(all_definitions)} total definitions")
        
        return True
    except Exception as e:
        print(f"❌ Error rebuilding database: {e}")
        return False

if __name__ == "__main__":
    success = rebuild_database()
    sys.exit(0 if success else 1)
