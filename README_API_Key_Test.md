# OpenAI API Key Tester

Test multiple OpenAI API keys quickly to see which ones are working.

## 🚀 Quick Start

### Option 1: Simple Version (Recommended)
```bash
# Install required package
pip install openai

# Run the simple tester
python simple_openai_test.py
```

### Option 2: Advanced Version (Faster, Concurrent)
```bash
# Install required packages
pip install -r requirements_openai_test.txt

# Run the advanced tester
python test_openai_keys.py
```

## 📋 Features

### Simple Version (`simple_openai_test.py`)
- ✅ Easy to use
- ✅ No external dependencies except OpenAI
- ✅ Clear error messages
- ✅ Saves working keys to file
- ✅ Tests keys sequentially

### Advanced Version (`test_openai_keys.py`)
- ✅ Tests keys concurrently (much faster)
- ✅ Response time measurement
- ✅ Detailed error reporting
- ✅ Progress tracking
- ✅ Saves detailed results to file
- ✅ Connection pooling for efficiency

## 🔧 Usage

1. **Run the script**
2. **Enter your API keys** one per line
3. **Press Enter** on empty line when done
4. **View results** showing which keys work
5. **Optionally save** working keys to file

## 📊 Example Output

```
🔑 OpenAI API Key Tester
========================================
Testing Key 1...
✅ Key 1 (sk-proj-...abcd): WORKING
   Response: Hello

Testing Key 2...
❌ Key 2 (sk-proj-...efgh): FAILED
   Error: Invalid API key

========================================
📊 SUMMARY
========================================
Total tested: 2
Working: 1
Failed: 1
Success rate: 50.0%

🎉 WORKING KEYS:
1. sk-proj-...abcd
```

## 🔍 Error Types Detected

- **Invalid API key** - Key is incorrect or expired
- **Rate limit exceeded** - Too many requests
- **API error** - OpenAI service issues
- **Connection error** - Network problems
- **Timeout** - Request took too long

## 💾 Output Files

- `working_openai_keys_YYYYMMDD_HHMMSS.txt` - List of working keys
- `openai_key_test_results_YYYYMMDD_HHMMSS.txt` - Detailed test results (advanced version)

## 🛡️ Security

- Keys are masked in output (only first 7 and last 4 characters shown)
- No keys are sent to third-party services
- Test only communicates with OpenAI's official API

## 📝 Requirements

- Python 3.7+
- Valid OpenAI API keys
- Internet connection

## ⚡ Performance

- **Simple version**: ~2 seconds per key
- **Advanced version**: ~0.5 seconds per key (concurrent)

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install openai
```

### "Invalid API key" for all keys
- Check if keys are copied correctly
- Ensure keys start with 'sk-'
- Verify OpenAI account is active

### Connection timeout
- Check internet connection
- Try the advanced version with better timeout handling

## 📄 License

MIT License - Feel free to use and modify!
