#!/usr/bin/env python3
"""
OpenAI API Key Validator
Tests multiple OpenAI API keys to check which ones are working
"""

import asyncio
import aiohttp
import json
import time
from typing import List, Dict, Tuple
from datetime import datetime

class OpenAIKeyValidator:
    def __init__(self):
        self.base_url = "https://api.openai.com/v1"
        self.test_prompt = "Say 'Hello, this is working!' in exactly this format."
        
    async def test_single_key(self, session: aiohttp.ClientSession, api_key: str) -> Tuple[str, bool, str, float]:
        """
        Test a single OpenAI API key
        
        Args:
            session: aiohttp session
            api_key: OpenAI API key to test
            
        Returns:
            Tuple of (api_key, is_working, response/error, response_time)
        """
        start_time = time.time()
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": self.test_prompt}
            ],
            "max_tokens": 50,
            "temperature": 0
        }
        
        try:
            async with session.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                response_time = time.time() - start_time
                
                if response.status == 200:
                    result = await response.json()
                    content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                    return api_key, True, content.strip(), response_time
                else:
                    error_text = await response.text()
                    try:
                        error_json = json.loads(error_text)
                        error_msg = error_json.get('error', {}).get('message', error_text)
                    except:
                        error_msg = error_text
                    return api_key, False, f"HTTP {response.status}: {error_msg}", response_time
                    
        except asyncio.TimeoutError:
            return api_key, False, "Request timeout (30s)", time.time() - start_time
        except aiohttp.ClientError as e:
            return api_key, False, f"Connection error: {str(e)}", time.time() - start_time
        except Exception as e:
            return api_key, False, f"Unexpected error: {str(e)}", time.time() - start_time
    
    async def test_multiple_keys(self, api_keys: List[str]) -> Dict:
        """
        Test multiple API keys concurrently
        
        Args:
            api_keys: List of OpenAI API keys to test
            
        Returns:
            Dictionary with test results
        """
        print(f"🔑 Testing {len(api_keys)} OpenAI API keys...")
        print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # Create connector with connection pooling
        connector = aiohttp.TCPConnector(
            limit=10,  # Maximum concurrent connections
            limit_per_host=5,  # Maximum connections per host
            ttl_dns_cache=300,
            use_dns_cache=True,
        )
        
        timeout = aiohttp.ClientTimeout(total=60)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            tasks = [self.test_single_key(session, key) for key in api_keys]
            results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process results
        working_keys = []
        failed_keys = []
        
        for result in results:
            if isinstance(result, Exception):
                failed_keys.append(("Unknown", False, f"Task failed: {str(result)}", 0))
            else:
                api_key, is_working, message, response_time = result
                if is_working:
                    working_keys.append((api_key, message, response_time))
                else:
                    failed_keys.append((api_key, False, message, response_time))
        
        return {
            'working_keys': working_keys,
            'failed_keys': failed_keys,
            'total_tested': len(api_keys),
            'working_count': len(working_keys),
            'failed_count': len(failed_keys)
        }
    
    def print_results(self, results: Dict):
        """Print test results in a formatted way"""
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS")
        print("=" * 60)
        
        print(f"📈 Total keys tested: {results['total_tested']}")
        print(f"✅ Working keys: {results['working_count']}")
        print(f"❌ Failed keys: {results['failed_count']}")
        print(f"📊 Success rate: {(results['working_count']/results['total_tested']*100):.1f}%")
        
        if results['working_keys']:
            print(f"\n🎉 WORKING KEYS ({len(results['working_keys'])}):")
            print("-" * 40)
            for i, (key, response, response_time) in enumerate(results['working_keys'], 1):
                masked_key = f"{key[:7]}...{key[-4:]}" if len(key) > 11 else "***MASKED***"
                print(f"{i}. {masked_key}")
                print(f"   Response: {response}")
                print(f"   Time: {response_time:.2f}s")
                print()
        
        if results['failed_keys']:
            print(f"❌ FAILED KEYS ({len(results['failed_keys'])}):")
            print("-" * 40)
            for i, (key, _, error, response_time) in enumerate(results['failed_keys'], 1):
                masked_key = f"{key[:7]}...{key[-4:]}" if len(key) > 11 else "***MASKED***"
                print(f"{i}. {masked_key}")
                print(f"   Error: {error}")
                print(f"   Time: {response_time:.2f}s")
                print()
        
        print("=" * 60)
        print(f"🏁 Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main function to run the API key validator"""
    
    print("🔑 OpenAI API Key Validator")
    print("=" * 60)
    
    # Option 1: Hardcoded keys (for testing)
    # api_keys = [
    #     "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    #     "sk-proj-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    #     # Add more keys here
    # ]
    
    # Option 2: Read from user input
    print("📝 Enter your OpenAI API keys (one per line).")
    print("   Press Enter on empty line to finish:")
    
    api_keys = []
    while True:
        api_key = input(f"Key {len(api_keys) + 1}: ").strip()
        if not api_key:
            break
        if api_key.startswith('sk-'):
            api_keys.append(api_key)
        else:
            print("⚠️  Warning: Key should start with 'sk-'")
    
    if not api_keys:
        print("❌ No API keys provided. Exiting.")
        return
    
    # Option 3: Read from file
    # Uncomment to use file input
    # try:
    #     with open('api_keys.txt', 'r') as f:
    #         api_keys = [line.strip() for line in f if line.strip().startswith('sk-')]
    # except FileNotFoundError:
    #     print("❌ api_keys.txt not found")
    #     return
    
    # Create validator and run tests
    validator = OpenAIKeyValidator()
    
    try:
        results = asyncio.run(validator.test_multiple_keys(api_keys))
        validator.print_results(results)
        
        # Save results to file
        save_results = input("\n💾 Save results to file? (y/n): ").lower().strip()
        if save_results == 'y':
            filename = f"openai_key_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write("OpenAI API Key Test Results\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
                
                f.write(f"Total tested: {results['total_tested']}\n")
                f.write(f"Working: {results['working_count']}\n")
                f.write(f"Failed: {results['failed_count']}\n")
                f.write(f"Success rate: {(results['working_count']/results['total_tested']*100):.1f}%\n\n")
                
                if results['working_keys']:
                    f.write("WORKING KEYS:\n")
                    for i, (key, response, response_time) in enumerate(results['working_keys'], 1):
                        f.write(f"{i}. {key}\n")
                        f.write(f"   Response: {response}\n")
                        f.write(f"   Time: {response_time:.2f}s\n\n")
                
                if results['failed_keys']:
                    f.write("FAILED KEYS:\n")
                    for i, (key, _, error, response_time) in enumerate(results['failed_keys'], 1):
                        f.write(f"{i}. {key}\n")
                        f.write(f"   Error: {error}\n")
                        f.write(f"   Time: {response_time:.2f}s\n\n")
            
            print(f"✅ Results saved to: {filename}")
    
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
