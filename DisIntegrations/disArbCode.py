# Credential (decrypted) — key matches the credential's variable_name
bot_token = credential_value.get('bot_token')

# Inputs — handle both the plain value and the {"value": ...} wrapper
def _val(key, default=''):
    v = input_data.get(key, default)
    return v.get('value', default) if isinstance(v, dict) else v

channel_id = _val('channel_id')
content = _val('content')

if not bot_token:
    result = {'success': False, 'error': 'Missing bot_token in credentials'}
elif not channel_id or not content:
    result = {'success': False, 'error': 'channel_id and content are required'}
else:
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
    try:
        response = requests.post(
            url,
            headers={
                'Authorization': f'Bot {bot_token}',
                'Content-Type': 'application/json',
            },
            json={'content': content},
            timeout=30,
        )
        if response.status_code // 100 == 2:
            result = {'success': True, 'result': {'message': response.json()}}
        else:
            result = {'success': False,
                      'error': f'Discord API error: {response.status_code} - {response.text}'}
    except Exception as e:
        result = {'success': False, 'error': f'Request failed: {str(e)}'}