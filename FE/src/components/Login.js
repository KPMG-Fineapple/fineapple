import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { useRouter } from "next/router";
import { useState } from "react";

export default function Login({ updateLogin }) {
  const router = useRouter();

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
    console.log({
      email: data.get("email"),
      password: data.get("password"),
    });
  };

  const [signUp, setSignUp] = useState(false);
  const [address, setAddress] = useState(null);
  const handleLogin = () => {
    updateLogin(address);
    console.log(address);
  };

  return (
    <Container component="main" maxWidth="xs" style={{ marginTop: "20vh" }}>
      {!signUp ? (
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            로그인
          </Typography>
          <Box
            component="form"
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}
          >
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="아이디"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="비밀번호"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              onClick={() => router.push("/dashboard")}
            >
              로그인하기
            </Button>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              onClick={() => router.push("/dashboard")}
            >
              처음 오셨어요? 우리집 예상 수익률 계산하기
            </Button>
          </Box>
        </Box>
      ) : (
        <Box
          component="form"
          onSubmit={handleSubmit}
          noValidate
          sx={{ mt: 30 }}
        >
          <TextField
            margin="normal"
            required
            fullWidth
            name="address"
            label="거주하시는 주소를 입력해주세요"
            onChange={(e) => setAddress(e.target.value)}
            id="address"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={handleLogin}
          >
            예측 결과 보러 가기
          </Button>
        </Box>
      )}
    </Container>
  );
}
