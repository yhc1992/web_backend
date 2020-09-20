// 配置
let dev = {
  safePaths: ['/login'],
  apiBaseURL: 'api',
  imgBaseUrl: 'http://118.25.127.8:8000/e-learning-app-api/',
  token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjJNd1kyYmpnNFdCYlhQMGoifQ',
  imgServer: ''
}

let pro = {
  safePaths: ['/login'],
  apiBaseURL: '/e-learning-app-api/index.php/api/mob/v1/api',
  imgBaseUrl: 'http://118.25.127.8:8000/e-learning-app-api/',
  token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjJNd1kyYmpnNFdCYlhQMGoifQ"',
  imgServer: ''
}

export default process.env.NODE_ENV === 'development' ? dev : pro
