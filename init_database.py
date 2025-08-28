#!/usr/bin/env python3
"""
Initialize vector database with PRMSU student handbook data
This script runs during Railway deployment to populate the database
"""

import os
import sys
from definition_chunker import DefinitionChunker

def initialize_database():
    """Initialize the vector database with all definition files."""
    print("🚀 Initializing vector database for Railway deployment...")
    
    # Get database path from environment
    db_path = os.getenv("DB_PATH", "./vector_db")
    collection_name = "definitions"
    
    # Ensure directory exists
    os.makedirs(db_path, exist_ok=True)
    
    try:
        # Initialize chunker
        chunker = DefinitionChunker(db_path=db_path, collection_name=collection_name)
        print(f"✅ Database initialized at: {db_path}")
        
        # List of definition files to load
        definition_files = [
            "individual_definition.txt",
            "critical_university_info.txt",
            "comprehensive_fixes.txt",
            "corrections_and_additions.txt",
            "advanced_question_fixes.txt",
            "uniform_and_assistant_fixes.txt",
            "liquor_offense_penalties.txt",
            "private_scholarship_fix.txt",
            "prmsu_location_info.txt",
            "type_of_cross_enrollment.txt",
            "inbound_cross_enrolment.txt"
        ]
        
        total_chunks = 0
        successful_files = 0
        
        for filename in definition_files:
            if os.path.exists(filename):
                try:
                    print(f"📄 Processing: {filename}")
                    chunks_added = chunker.process_file(filename)
                    total_chunks += chunks_added
                    successful_files += 1
                    print(f"   ✅ Added {chunks_added} chunks")
                except Exception as e:
                    print(f"   ❌ Error processing {filename}: {e}")
            else:
                print(f"   ⚠️  File not found: {filename}")
        
        print(f"\n📊 DATABASE INITIALIZATION COMPLETE:")
        print(f"   Files processed: {successful_files}/{len(definition_files)}")
        print(f"   Total chunks added: {total_chunks}")
        
        # Verify database content
        all_definitions = chunker.list_all_definitions()
        print(f"   Database contains: {len(all_definitions)} definitions")
        
        if total_chunks > 0:
            print("✅ Database initialization successful!")
            return True
        else:
            print("❌ No data was loaded into the database!")
            return False
            
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

def check_database_health():
    """Check if the database is healthy and contains data."""
    db_path = os.getenv("DB_PATH", "./vector_db")
    collection_name = "definitions"
    
    try:
        chunker = DefinitionChunker(db_path=db_path, collection_name=collection_name)
        definitions = chunker.list_all_definitions()
        
        print(f"🔍 Database health check:")
        print(f"   Path: {db_path}")
        print(f"   Definitions: {len(definitions)}")
        
        if len(definitions) > 0:
            print("✅ Database is healthy!")
            return True
        else:
            print("⚠️  Database is empty!")
            return False
            
    except Exception as e:
        print(f"❌ Database health check failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        # Health check mode
        success = check_database_health()
    else:
        # Initialization mode
        success = initialize_database()
    
    sys.exit(0 if success else 1)
