import * as React from "react";
import { styled } from "@mui/material/styles";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import ButtonBase from "@mui/material/ButtonBase";
import Stack from "@mui/material/Stack";
import { useRouter } from "next/router";

const Img = styled("img")({
  margin: "auto",
  display: "block",
  maxWidth: "100%",
  maxHeight: "100%",
});

export default function Card({ imgURL, num }) {
  const router = useRouter();
  const imgSrc = num === 3 ? imgURL + ".png" : imgURL + ".jpeg";
  console.log(imgSrc);

  return (
    <Paper
      sx={{
        p: 2,
        margin: "auto",
        maxWidth: 700,
        flexGrow: 1,
        backgroundColor: (theme) =>
          theme.palette.mode === "dark" ? "#1A2027" : "#fff",
      }}
    >
      <Grid container spacing={2}>
        <Stack spacing={0} sx={{ marginLeft: 2 }}>
          <ButtonBase sx={{ width: 150, height: 180 }}>
            <Img alt="complex" src={imgSrc} />
          </ButtonBase>
        </Stack>
        <Grid item xs={12} sm container sx={{ marginTop: 4 }}>
          <Grid item xs container direction="column" spacing={2}>
            <Grid item xs>
              <Typography gutterBottom variant="subtitle1" component="div">
                이름
              </Typography>
              <Typography variant="body2" gutterBottom>
                내용 내용 내용 내용 내용 내용
              </Typography>
            </Grid>
            <Grid item sx={{ marginLeft: 4 }}>
              <Button
                onClick={() => router.push(`/invest/items/item${num}`)}
                variant="contained"
                sx={{ padding: 1 }}
              >
                자세히 알아보기{" "}
              </Button>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Paper>
  );
}
