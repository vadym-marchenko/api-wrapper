import rest

def test_get_bearer_token_success():
    grant_type = 'password'
    client_id = '48d614dc80bcb154d718d3e38f0d8430'
    client_secret = 'MfW,.jqU_[Qj(<)=0T*vV76srLSDBX.YM02=:13s'
    username = 'usm.connector'
    password = 'Secret123!@!'
    token_url = 'https://interxionacc.service-now.com/oauth_token'
    sut = rest.Rest()
    print(sut.get_bearer_token(grant_type, client_id, client_secret, username, password, token_url))
