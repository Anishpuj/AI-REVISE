#!/usr/bin/env python3
"""
Simple OpenAI API Key Tester
Quick test multiple API keys to see which ones work
"""

import openai
import time
from datetime import datetime

def test_openai_key(api_key, key_num):
    """Test a single OpenAI API key"""
    print(f"Testing Key {key_num}...")
    
    try:
        # Set the API key
        client = openai.OpenAI(api_key=api_key)
        
        # Make a simple API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello'"}],
            max_tokens=10
        )
        
        # If we get here, the key works
        result = response.choices[0].message.content
        return True, result, None
        
    except openai.AuthenticationError as e:
        return False, None, "Invalid API key"
    except openai.RateLimitError as e:
        return False, None, "Rate limit exceeded"
    except openai.APIError as e:
        return False, None, f"API error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"

def main():
    print("🔑 OpenAI API Key Tester")
    print("=" * 40)
    
    # Get API keys from user
    api_keys = []
    print("Enter your OpenAI API keys (press Enter on empty line to finish):")
    
    while True:
        key = input(f"Key {len(api_keys) + 1}: ").strip()
        if not key:
            break
        if key.startswith('sk-'):
            api_keys.append(key)
        else:
            print("⚠️  Key should start with 'sk-'")
    
    if not api_keys:
        print("❌ No keys provided!")
        return
    
    print(f"\n🧪 Testing {len(api_keys)} API keys...\n")
    
    working_keys = []
    failed_keys = []
    
    start_time = time.time()
    
    for i, key in enumerate(api_keys, 1):
        is_working, response, error = test_openai_key(key, i)
        
        masked_key = f"{key[:7]}...{key[-4:]}" if len(key) > 11 else "***MASKED***"
        
        if is_working:
            print(f"✅ Key {i} ({masked_key}): WORKING")
            print(f"   Response: {response}")
            working_keys.append(key)
        else:
            print(f"❌ Key {i} ({masked_key}): FAILED")
            print(f"   Error: {error}")
            failed_keys.append((key, error))
        
        print()
    
    end_time = time.time()
    
    # Summary
    print("=" * 40)
    print("📊 SUMMARY")
    print("=" * 40)
    print(f"Total tested: {len(api_keys)}")
    print(f"Working: {len(working_keys)}")
    print(f"Failed: {len(failed_keys)}")
    print(f"Success rate: {len(working_keys)/len(api_keys)*100:.1f}%")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    if working_keys:
        print(f"\n🎉 WORKING KEYS:")
        for i, key in enumerate(working_keys, 1):
            masked_key = f"{key[:7]}...{key[-4:]}" if len(key) > 11 else "***MASKED***"
            print(f"{i}. {masked_key}")
    
    if failed_keys:
        print(f"\n❌ FAILED KEYS:")
        for i, (key, error) in enumerate(failed_keys, 1):
            masked_key = f"{key[:7]}...{key[-4:]}" if len(key) > 11 else "***MASKED***"
            print(f"{i}. {masked_key} - {error}")
    
    # Save working keys to file
    if working_keys:
        save = input("\n💾 Save working keys to file? (y/n): ").lower()
        if save == 'y':
            filename = f"working_openai_keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                for key in working_keys:
                    f.write(key + '\n')
            print(f"✅ Saved {len(working_keys)} working keys to {filename}")

if __name__ == "__main__":
    main()
