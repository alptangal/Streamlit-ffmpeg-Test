import { Client } from "discord.js-selfbot-v13";
import { Streamer,streamLivestreamVideo } from '@dank074/discord-video-stream';

const streamer = new Streamer(new Client());
await streamer.client.login(process.env.botToken);
await streamer.joinVoice("1122707918177960047", "1200346808552001538");

const udp = await streamer.createStream({
    "width": 1920,
    "height": 1080,
    "fps": 24,
    "bitrateKbps": 2500,
    "maxBitrateKbps": 2500,
    "hardware_acc": false,
    "videoCodec": "H264"
});
udp.mediaConnection.setSpeaking(true);
udp.mediaConnection.setVideoStatus(true);
try {
    const res = await streamLivestreamVideo(process.env.url, udp);

    console.log("Finished playing video " + res);
} catch (e) {
    console.log(e);
} finally {
    udp.mediaConnection.setSpeaking(false);
    udp.mediaConnection.setVideoStatus(false);
}