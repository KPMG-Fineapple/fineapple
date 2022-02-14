import { Button } from "@mui/material";
import Grid from "@mui/material/Grid";
import Image from "next/image";
import Typography from "@mui/material/Typography";
import { useRouter } from "next/router";

function Main() {
  const router = useRouter();

  return (
    <Grid
      container
      justify="center"
      alignItems="center"
      direction="column"
      style={{ marginTop: "20vh" }}
      spacing={5}
    >
      <Grid item>
        <Image src="/static/logo2.svg" alt="logo" width="192" height="192" />
      </Grid>
      <Grid item>
        <Typography component="h1" variant="h5">
          원하시는 서비스를 선택해주세요
        </Typography>
        <Grid item>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={() => router.push("/home/main")}
          >
            가정용
          </Button>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={() => router.push("/home/main")}
          >
            투자용
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default Main;
