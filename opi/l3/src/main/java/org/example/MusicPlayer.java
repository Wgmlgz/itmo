package org.example;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.advanced.AdvancedPlayer;

import java.io.FileInputStream;
import java.io.IOException;

public class MusicPlayer {
    public static void main(String[] args) {
        String filePath = "sound.mp3";
        try (FileInputStream fileInputStream = new FileInputStream(filePath)) {
            AdvancedPlayer player = new AdvancedPlayer(fileInputStream);
            player.play();
        } catch (IOException | JavaLayerException e) {
            e.printStackTrace();
        }
    }

}
