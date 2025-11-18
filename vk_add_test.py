from libs.vk.vk import VK, VKExceptions

# Proxy configuration
proxy_connection = 'https://u327dc3fc51bf0599-zone-custom-region-ru:u327dc3fc51bf0599@165.154.179.147:2333'

vk = VK()
vk.set_proxy(proxy_connection)

if __name__ == '__main__':
    try:
        auth = vk.auth('79010466328', 'Ddr0B4fS1a1FdQ')

        if auth:
            print('✅ Authentication successful!')
            print(f'Access token: {auth.get("access_token", "N/A")[:20]}...')
            print(f'User ID: {auth.get("user_id", "N/A")}')
        else:
            print('⚠️ Authentication returned None — возможно, авторизация прервалась или капча не решена.')

    except VKExceptions.APIError as e:
        print('❌ VK API Error!')
        print(f'Error Code: {e.code}')
        print(f'Error Message: {e.msg}')
        print(f'Full error: {e.to_dict()}')
    except Exception as e:
        print(f'⚠️ Unexpected error: {e}')
