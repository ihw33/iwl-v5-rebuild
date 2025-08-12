# IWL v5.0 API 명세 (초안)

## 공통
- Base URL: `/api`
- Auth: Bearer JWT (예정)
- 응답 형식: `application/json`

## Auth
- POST `/auth/register`
  - body: { email, password, name }
  - 201: { user }
- POST `/auth/login`
  - body: { email, password }
  - 200: { token, user }
- POST `/auth/logout`
  - 204
- GET `/auth/me`
  - 200: { user }

## Matrix
- GET `/matrix`
  - query: { page?, size?, tag? }
  - 200: { items: MatrixItem[], total }
- GET `/matrix/:id`
  - 200: MatrixItem
- POST `/matrix`
  - body: Partial<MatrixItem>
  - 201: MatrixItem
- PATCH `/matrix/:id`
  - body: Partial<MatrixItem>
  - 200: MatrixItem
- DELETE `/matrix/:id`
  - 204

## Progress
- GET `/progress?itemId=&userId=`
  - 200: Progress[]
- POST `/progress`
  - body: { itemId, status }
  - 201: Progress
- PATCH `/progress/:id`
  - body: { status }
  - 200: Progress

## 타입
```ts
export type MatrixItem = {
  id: string
  row: number
  col: number
  title: string
  content: string
  tags?: string[]
  progress?: number // 0-100
}

export type Progress = {
  id: string
  userId: string
  itemId: string
  status: 'todo' | 'doing' | 'done'
  updatedAt: string
}
```
