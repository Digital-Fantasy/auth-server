from python_graphql_client import GraphqlClient
import utils
# Instantiate the client with an endpoint.

endpoint = utils.get_env_var("GRAPHQL_ENDPOINT")
gql = GraphqlClient(endpoint=endpoint)
